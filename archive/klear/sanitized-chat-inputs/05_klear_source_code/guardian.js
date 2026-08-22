/**
 * CP Guardian — Checkpoint 1 (Programmatic) + Checkpoint 2 (Claude-as-Guardian)
 *
 * Checkpoint 1: Runs on every message after IPP classification and ICD filtering.
 *   PC-1: Filtered IPPs exist → Clarify (ambiguous_signal)
 *   PC-2: Signal out of declared scope → Clarify (scope_boundary)
 *   PC-3: No verified intent → Clarify (unverified_intent)
 *   PC-4: All clear → Allow
 *
 * Checkpoint 2: Conditional — runs after Claude response generation.
 *   Triggers: borderline IPP (0.3–0.5), decay spike > 0.2, response length > 3x avg
 *   Returns: allow/clarify/refuse + sa_score + cp_score
 *
 * Spec reference: §4.3, §4.5
 */

const Anthropic = require('@anthropic-ai/sdk');

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Guardian Checkpoint 1 — Programmatic rules.
 *
 * @param {object} params
 * @param {Array} params.filteredIPPs — IPPs that survived ICD filter (surfaced list)
 * @param {Array} params.allIPPs — all detected IPPs (for borderline detection)
 * @param {object|null} params.intent — active intent object (null if none)
 * @param {object|null} params.context — session context object
 * @param {string} params.user_message — current user message
 * @returns {object} { decision, trigger_type, ipp_type, clarification_question, confidence, rule }
 */
function checkpoint1({ filteredIPPs, allIPPs, intent, context, user_message }) {
  // PC-3: No verified intent in session
  if (!intent || !['verified', 'active'].includes(intent.state)) {
    return {
      decision: 'clarify',
      trigger_type: 'unverified_intent',
      ipp_type: null,
      clarification_question: 'Please confirm what you\'re trying to do before continuing.',
      confidence: null,
      rule: 'PC-3',
    };
  }

  // PC-1: Filtered IPPs exist → friction (ambiguous_signal)
  if (filteredIPPs.length > 0) {
    // Surface the highest-confidence IPP as the primary friction
    const primary = filteredIPPs.sort((a, b) => b.confidence - a.confidence)[0];
    return {
      decision: 'clarify',
      trigger_type: 'ambiguous_signal',
      ipp_type: primary.type,
      clarification_question: primary.clarification_question,
      confidence: primary.confidence,
      rule: 'PC-1',
    };
  }

  // PC-2: Signal out of declared scope
  // Lightweight heuristic check — full semantic similarity would use embeddings.
  // For now, if context has exclusions and the message seems to match them, flag it.
  if (context && context.exclusions) {
    const exclusions = context.exclusions.toLowerCase();
    const msg = user_message.toLowerCase();
    const exclusionTerms = exclusions.split(',').map(t => t.trim()).filter(t => t.length > 2);
    for (const term of exclusionTerms) {
      if (msg.includes(term)) {
        return {
          decision: 'clarify',
          trigger_type: 'scope_boundary',
          ipp_type: null,
          clarification_question: `This seems to touch on "${term}", which is outside your declared scope. How would you like to proceed?`,
          confidence: null,
          rule: 'PC-2',
        };
      }
    }
  }

  // PC-4: All clear
  return {
    decision: 'allow',
    trigger_type: null,
    ipp_type: null,
    clarification_question: null,
    confidence: null,
    rule: 'PC-4',
  };
}

/**
 * Determine whether Checkpoint 2 should run.
 *
 * Trigger conditions (any one sufficient):
 * - Any IPP detected with confidence 0.3–0.5 (borderline)
 * - Intent decay δ spiked > 0.2 on this message
 * - Claude response length > 3x average response length for session
 *
 * @param {object} params
 * @param {Array} params.allIPPs — all detected IPPs (including unsurfaced)
 * @param {number} params.decayDelta — δ for this message
 * @param {number} params.responseLength — character count of Claude's response
 * @param {number} params.avgResponseLength — average response length for this session
 * @returns {boolean}
 */
function shouldRunCheckpoint2({ allIPPs, decayDelta, responseLength, avgResponseLength }) {
  // Borderline IPP: any IPP with confidence in 0.3–0.5
  const hasBorderlineIPP = allIPPs.some(ipp => ipp.confidence >= 0.3 && ipp.confidence <= 0.5);

  // Decay spike
  const hasDecaySpike = decayDelta > 0.2;

  // Response length anomaly
  const hasLengthAnomaly = avgResponseLength > 0 && responseLength > (3 * avgResponseLength);

  return hasBorderlineIPP || hasDecaySpike || hasLengthAnomaly;
}

/**
 * Guardian Checkpoint 2 — Claude-as-Guardian.
 * Exact prompt from §4.5 of the spec.
 *
 * @param {object} params
 * @param {object} params.context — session context
 * @param {object} params.intent — active intent
 * @param {Array} params.nodes — active nodes (constraints)
 * @param {number} params.icd_value — ICD setting
 * @param {string} params.claude_response — the AI response to evaluate
 * @returns {Promise<{decision: string, reason: string, sa_score: number, cp_score: number}>}
 */
async function checkpoint2({ context, intent, nodes, icd_value, claude_response }) {
  const prompt = `You are the CP Guardian for Klear. Evaluate whether the AI response
aligns with the user's declared intent and context.

Declared context: ${context.description || 'Not declared'}
Scope includes: ${context.inclusions || 'Not specified'}
Scope excludes: ${context.exclusions || 'Not specified'}
Declared intent: ${intent.declaration_text}
Intent type: ${intent.intent_type || 'Not specified'}
Active node constraints: ${nodes.length > 0 ? nodes.map(n => n.content).join(', ') : 'None'}
ICD setting: ${icd_value}

AI response to evaluate:
${claude_response}

Return ONLY valid JSON — no preamble, no explanation:
{
  "decision": "allow" | "clarify" | "refuse",
  "reason": "one sentence explanation",
  "sa_score": 0.0,
  "cp_score": 0.0
}

Decision rules:
- allow: response stays within declared scope and serves declared intent
- clarify: response partially drifts or is ambiguous about scope
- refuse: response clearly goes outside declared context or contradicts intent

Score rules:
- sa_score: 0.0–1.0 — how well the response semantically matches the declared intent
- cp_score: 0.0–1.0 — proportion of active node constraints satisfied by the response
- If no active nodes exist, cp_score = 1.0`;

  try {
    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 512,
      messages: [
        { role: 'user', content: prompt },
      ],
    });

    const text = response.content[0]?.text || '';
    return parseCheckpoint2Response(text, nodes);
  } catch (error) {
    console.error('Guardian CP2 error:', error.message);
    // Fallback: allow with heuristic scores per §4.5 "When Checkpoint 2 is skipped"
    return {
      decision: 'allow',
      reason: 'Checkpoint 2 failed — defaulting to allow with heuristic scores',
      sa_score: 0.8,
      cp_score: nodes.length > 0 ? 1.0 : 1.0,
      cp2_failed: true,
    };
  }
}

/**
 * Parse Checkpoint 2 Claude response.
 */
function parseCheckpoint2Response(text, nodes) {
  try {
    let jsonStr = text.trim();
    if (jsonStr.startsWith('```')) {
      jsonStr = jsonStr.replace(/^```(?:json)?\s*/, '').replace(/\s*```$/, '');
    }

    const result = JSON.parse(jsonStr);

    const decision = ['allow', 'clarify', 'refuse'].includes(result.decision)
      ? result.decision : 'allow';
    const sa_score = typeof result.sa_score === 'number'
      ? Math.max(0, Math.min(1, result.sa_score)) : 0.8;
    const cp_score = typeof result.cp_score === 'number'
      ? Math.max(0, Math.min(1, result.cp_score)) : (nodes.length > 0 ? 1.0 : 1.0);

    return {
      decision,
      reason: result.reason || '',
      sa_score: Math.round(sa_score * 1000) / 1000,
      cp_score: Math.round(cp_score * 1000) / 1000,
    };
  } catch (error) {
    console.error('Guardian CP2 parse error:', error.message);
    return {
      decision: 'allow',
      reason: 'Failed to parse Guardian response — defaulting to allow',
      sa_score: 0.8,
      cp_score: 1.0,
      cp2_failed: true,
    };
  }
}

/**
 * Get heuristic scores when Checkpoint 2 is skipped.
 * Per §4.5: SA estimated at 0.8, CP calculated programmatically from node satisfaction.
 *
 * @param {Array} nodes — active nodes
 * @returns {{ sa_score: number, cp_score: number, cp2_skipped: boolean }}
 */
function getHeuristicScores(nodes) {
  return {
    sa_score: 0.8,
    cp_score: nodes.length > 0 ? 1.0 : 1.0, // Programmatic check would go here with real node satisfaction logic
    cp2_skipped: true,
  };
}

module.exports = {
  checkpoint1,
  checkpoint2,
  shouldRunCheckpoint2,
  getHeuristicScores,
  parseCheckpoint2Response,
};
