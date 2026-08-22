/**
 * IFI Calculator — Intent Fidelity Index
 *
 * IFI = 0.4(SA) + 0.3(CP) + 0.3(SS)
 *
 * Phase 1 (immediate): SA and CP from Guardian Checkpoint 2 (or heuristics)
 * Phase 2 (post-rating): SS from user's 1–5 star rating, normalized to 0–1
 *
 * SS normalization: (stars - 1) / 4
 *
 * Spec reference: §4.7
 */

const db = require('../db/supabase');

const WEIGHTS = { sa: 0.4, cp: 0.3, ss: 0.3 };

/**
 * Calculate Phase 1 IFI (SA + CP, SS pending).
 * Stores partial score in DB.
 *
 * @param {object} params
 * @param {string} params.session_id
 * @param {string} params.action_id
 * @param {number} params.sa_score
 * @param {number} params.cp_score
 * @param {boolean} params.cp2_skipped
 * @returns {Promise<object>} stored IFI record
 */
async function calculatePhase1({ session_id, action_id, sa_score, cp_score, cp2_skipped = false }) {
  // Phase 1 composite excludes SS — show partial weighted score
  const partial = (WEIGHTS.sa * sa_score) + (WEIGHTS.cp * cp_score);

  const record = await db.createIFIScore({
    session_id,
    action_id,
    sa_score,
    cp_score,
    ss_score: null,
    composite: null, // Full composite only after SS rating
    pending_ss: true,
    cp2_skipped,
  });

  return {
    ...record,
    partial_score: Math.round(partial * 1000) / 1000,
    display: `SA: ${sa_score.toFixed(2)} | CP: ${cp_score.toFixed(2)} | SS: pending`,
  };
}

/**
 * Calculate Phase 2 IFI after user submits satisfaction rating.
 *
 * @param {string} action_id
 * @param {number} ss_stars — 1–5 star rating
 * @returns {Promise<object>} updated IFI record with composite
 */
async function calculatePhase2(action_id, ss_stars) {
  const existing = await db.getIFIByAction(action_id);
  if (!existing) {
    throw new Error(`No IFI record found for action ${action_id}`);
  }

  // Normalize 1–5 stars to 0–1
  const ss_score = Math.max(0, Math.min(1, (parseInt(ss_stars) - 1) / 4));

  const sa = parseFloat(existing.sa_score);
  const cp = parseFloat(existing.cp_score);
  const composite = (WEIGHTS.sa * sa) + (WEIGHTS.cp * cp) + (WEIGHTS.ss * ss_score);
  const rounded = Math.round(composite * 1000) / 1000;

  const updated = await db.updateIFIScore(existing.id, {
    ss_score,
    composite: rounded,
    pending_ss: false,
  });

  return {
    ...updated,
    composite: rounded,
    sa,
    cp,
    ss: ss_score,
    display: `IFI: ${rounded.toFixed(2)} (SA: ${sa.toFixed(2)}, CP: ${cp.toFixed(2)}, SS: ${ss_score.toFixed(2)})`,
  };
}

/**
 * Get IFI display data for an action.
 * Returns null if no IFI record exists.
 */
async function getIFIDisplay(action_id) {
  const record = await db.getIFIByAction(action_id);
  if (!record) return null;

  const sa = parseFloat(record.sa_score);
  const cp = parseFloat(record.cp_score);

  if (record.pending_ss) {
    return {
      composite: null,
      sa,
      cp,
      ss: null,
      pending_ss: true,
      cp2_skipped: record.cp2_skipped,
      display: `SA: ${sa.toFixed(2)} | CP: ${cp.toFixed(2)} | SS: pending`,
    };
  }

  return {
    composite: parseFloat(record.composite),
    sa,
    cp,
    ss: parseFloat(record.ss_score),
    pending_ss: false,
    cp2_skipped: record.cp2_skipped,
    display: `IFI: ${parseFloat(record.composite).toFixed(2)}`,
  };
}

/**
 * Get aggregate IFI statistics for a session (for CP Compliance Report).
 */
async function getSessionIFIStats(session_id) {
  const scores = await db.getIFIBySession(session_id);
  const completed = scores.filter(s => !s.pending_ss && s.composite !== null);

  if (completed.length === 0) {
    return { average: null, count: 0, trend: [] };
  }

  const values = completed.map(s => parseFloat(s.composite));
  const average = values.reduce((sum, v) => sum + v, 0) / values.length;

  return {
    average: Math.round(average * 1000) / 1000,
    count: completed.length,
    trend: values,
  };
}

module.exports = {
  calculatePhase1,
  calculatePhase2,
  getIFIDisplay,
  getSessionIFIStats,
  WEIGHTS,
};
