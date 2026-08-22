/**
 * Friction Manager
 *
 * Triggers and resolves CP friction events.
 * User action is always required to resolve — friction is never auto-resolved.
 *
 * Trigger types (spec §4.6):
 *   ambiguous_signal, unverified_intent, scope_boundary,
 *   permission_violation, high_risk_action, missing_context,
 *   conflict_detected, decay_warning
 *
 * Resolution types:
 *   user_clarified, user_confirmed, user_revised,
 *   user_abandoned, system_blocked
 */

const db = require('../db/supabase');
const { logEvent } = require('./logger');

const VALID_TRIGGERS = [
  'ambiguous_signal',
  'unverified_intent',
  'scope_boundary',
  'permission_violation',
  'high_risk_action',
  'missing_context',
  'conflict_detected',
  'decay_warning',
];

const VALID_RESOLUTIONS = [
  'user_clarified',
  'user_confirmed',
  'user_revised',
  'user_abandoned',
  'system_blocked',
];

/**
 * Trigger a friction event.
 * Creates DB record + audit log. Returns the friction card payload for UI.
 *
 * @param {object} params
 * @param {string} params.session_id
 * @param {string} params.user_id
 * @param {string} params.trigger_type
 * @param {string|null} params.ipp_type
 * @param {string} params.clarification_question
 * @param {number|null} params.confidence
 */
async function triggerFriction({
  session_id,
  user_id,
  trigger_type,
  ipp_type = null,
  clarification_question,
  confidence = null,
}) {
  if (!VALID_TRIGGERS.includes(trigger_type)) {
    console.warn(`Unknown friction trigger type: ${trigger_type}`);
  }

  const friction = await db.createFriction({
    session_id,
    trigger_type,
    ipp_type,
    clarification_question,
  });

  // Log to CP audit log
  await logEvent({
    session_id,
    user_id,
    event_type: 'friction',
    event_subtype: 'triggered',
    payload: {
      friction_id: friction.id,
      trigger_type,
      ipp_type,
      clarification_question,
      confidence,
    },
  });

  return {
    friction_id: friction.id,
    trigger_type,
    ipp_type,
    clarification_question,
    confidence,
    status: 'open',
    // UI hint based on trigger type
    severity: getSeverity(trigger_type),
  };
}

/**
 * Resolve a friction event. Only valid user actions resolve friction.
 *
 * @param {object} params
 * @param {string} params.session_id
 * @param {string} params.user_id
 * @param {string} params.friction_id
 * @param {string} params.resolution
 * @param {string|null} params.input — user's clarification/revision text
 */
async function resolveFriction({ session_id, user_id, friction_id, resolution, input = null }) {
  if (!VALID_RESOLUTIONS.includes(resolution)) {
    throw new Error(`Invalid friction resolution: ${resolution}`);
  }

  const updated = await db.resolveFriction(friction_id, resolution, input);

  // Log resolution to CP audit log
  await logEvent({
    session_id,
    user_id,
    event_type: 'friction',
    event_subtype: 'resolved',
    payload: {
      friction_id,
      resolution,
      input,
    },
  });

  return updated;
}

/**
 * Get UI severity for a friction trigger type.
 */
function getSeverity(trigger_type) {
  switch (trigger_type) {
    case 'high_risk_action':
    case 'permission_violation':
    case 'conflict_detected':
      return 'high';
    case 'scope_boundary':
    case 'decay_warning':
      return 'medium';
    default:
      return 'standard';
  }
}

module.exports = {
  triggerFriction,
  resolveFriction,
  getSeverity,
  VALID_TRIGGERS,
  VALID_RESOLUTIONS,
};
