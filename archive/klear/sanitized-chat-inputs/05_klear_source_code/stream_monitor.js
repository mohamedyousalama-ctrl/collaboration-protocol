/**
 * Stream Monitor — Guardian Checkpoint 1.5
 *
 * Mid-generation stream monitoring for real-time intent enforcement.
 * Evaluates partial Claude responses at ICD-controlled intervals to detect
 * scope violations, intent mismatches, and constraint violations during generation.
 *
 * CP v1.1 addition. Does NOT modify any CP v1.0.1 logic.
 *
 * Event routing:
 *   - stream.* events → Klear Events Store (writeKlearEvent / stream_monitor_log)
 *   - guardian.mid_generation → CP Log Store (via logger.logEvent)
 *   - NEVER write stream.* to CP Log Store
 *
 * Error handling: on any monitor evaluation error → fail safe to CONTINUE.
 * Never fail to abort on monitor errors.
 */

const Anthropic = require('@anthropic-ai/sdk');

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Get the token-count interval for stream monitoring based on ICD level.
 * Higher ICD = more frequent checks = smaller interval.
 *
 * @param {number} icd — user's ICD setting (0.0–1.0)
 * @returns {number} token count interval
 */
function getMonitorInterval(icd) {
  if (icd <= 0.2) return 400;
  if (icd <= 0.5) return 200;
  if (icd <= 0.8) return 80;
  return 30; // ICD 0.9–1.0
}

/**
 * Evaluate a partial response for intent/context drift.
 * Calls Claude as the Guardian Stream Monitor (Checkpoint 1.5).
 *
 * On ANY error → returns safe CONTINUE result. Never throws.
 *
 * @param {object} params
 * @param {string} params.partialResponse — accumulated response text so far
 * @param {number} params.tokenCount — total tokens generated so far
 * @param {object} params.context — session context { description, inclusions, exclusions }
 * @param {object} params.intent — active intent { declaration_text, intent_type }
 * @param {Array} params.nodes — active constraint nodes
 * @param {number} params.icd — ICD setting
 * @param {number} params.intervalNumber — which interval check this is (1, 2, 3...)
 * @returns {Promise<{decision: string, reason: string, drift_type: string, drift_confidence: number}>}
 */
async function evaluatePartialResponse({ partialResponse, tokenCount, context, intent, nodes, icd, intervalNumber }) {
  try {
    const nodesText = nodes && nodes.length > 0
      ? nodes.map(n => n.content).join(', ')
      : 'None';

    const prompt = `You are the CP Guardian Stream Monitor for Klear, operating at Checkpoint 1.5.

Your job is to evaluate whether the AI response generated so far is staying
within the user's declared intent and context boundaries.

Declared context: ${context?.description || 'Not declared'}
Scope includes: ${context?.inclusions || 'Not specified'}
Scope excludes: ${context?.exclusions || 'Not specified'}
Declared intent: ${intent?.declaration_text || 'Not declared'}
Intent type: ${intent?.intent_type || 'Not specified'}
Active constraints (nodes): ${nodesText}

Partial response generated so far (${tokenCount} tokens):
${partialResponse}

Evaluate ONLY whether this partial response, if continued in the same direction,
would violate the declared intent or context.

Return ONLY valid JSON — no preamble, no explanation, no markdown:
{
  "decision": "continue" | "abort",
  "reason": "one sentence explanation",
  "drift_type": "scope_violation" | "intent_mismatch" | "constraint_violation" | "none",
  "drift_confidence": 0.0
}

Field definitions:
- decision: "continue" if within boundaries, "abort" if drift detected
- reason: one sentence explaining the decision
- drift_type: category of drift. Use "none" when decision is "continue"
- drift_confidence: 0.0–1.0. Use 0.0 when continuing. Use 0.5–1.0 when aborting.

Only abort if drift is clear and significant. Do not abort for minor stylistic
differences. Abort when the response would produce content the user did not authorize.`;

    const response = await anthropic.messages.create({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 256,
      messages: [{ role: 'user', content: prompt }],
    });

    const text = response.content[0]?.text || '';
    return parseMonitorResponse(text);
  } catch (error) {
    // Fail safe to CONTINUE on any error — never fail to abort on monitor errors
    console.error('Stream monitor evaluation error:', error.message);
    return {
      decision: 'continue',
      reason: 'monitor_error',
      drift_type: 'none',
      drift_confidence: 0,
    };
  }
}

/**
 * Parse the monitor's JSON response. On parse failure → safe CONTINUE.
 */
function parseMonitorResponse(text) {
  try {
    let jsonStr = text.trim();
    if (jsonStr.startsWith('```')) {
      jsonStr = jsonStr.replace(/^```(?:json)?\s*/, '').replace(/\s*```$/, '');
    }
    const match = jsonStr.match(/\{[\s\S]*\}/);
    if (match) jsonStr = match[0];

    const result = JSON.parse(jsonStr);

    const decision = result.decision === 'abort' ? 'abort' : 'continue';
    const drift_type = ['scope_violation', 'intent_mismatch', 'constraint_violation', 'none'].includes(result.drift_type)
      ? result.drift_type : 'none';
    const drift_confidence = typeof result.drift_confidence === 'number'
      ? Math.max(0, Math.min(1, result.drift_confidence)) : 0;

    return {
      decision,
      reason: result.reason || '',
      drift_type: decision === 'continue' ? 'none' : drift_type,
      drift_confidence: Math.round(drift_confidence * 1000) / 1000,
    };
  } catch (error) {
    console.error('Stream monitor parse error:', error.message);
    return {
      decision: 'continue',
      reason: 'monitor_parse_error',
      drift_type: 'none',
      drift_confidence: 0,
    };
  }
}

module.exports = {
  getMonitorInterval,
  evaluatePartialResponse,
  parseMonitorResponse,
};
