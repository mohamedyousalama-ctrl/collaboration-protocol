/**
 * ICD Filter — Intent Control Degree
 *
 * User's ICD value (0.0–1.0) determines which detected IPPs get surfaced.
 * Threshold = 1 - ICD.
 * IPPs with confidence >= threshold are surfaced (friction).
 * IPPs below threshold are auto-resolved by Claude.
 *
 * Presets:
 *   Fast     ICD=0.2 → threshold=0.8 → only very high confidence IPPs surface
 *   Balanced ICD=0.5 → threshold=0.5 → medium+ confidence IPPs surface
 *   Precise  ICD=0.8 → threshold=0.2 → nearly all IPPs surface
 *
 * Spec reference: §4.2
 */

/**
 * Apply ICD filter to detected IPPs.
 * @param {Array} ipps — output from classifyIPP()
 * @param {number} icd — user's ICD setting (0.0–1.0)
 * @returns {{ surfaced: Array, unsurfaced: Array, threshold: number }}
 */
function applyICDFilter(ipps, icd) {
  const clampedICD = Math.max(0, Math.min(1, parseFloat(icd) || 0));
  const threshold = Math.round((1 - clampedICD) * 100) / 100;

  const surfaced = [];
  const unsurfaced = [];

  for (const ipp of ipps) {
    if (ipp.confidence >= threshold) {
      surfaced.push({ ...ipp, surfaced: true });
    } else {
      unsurfaced.push({ ...ipp, surfaced: false });
    }
  }

  return { surfaced, unsurfaced, threshold };
}

/**
 * Get human-readable label for an ICD value.
 */
function getICDLabel(icd) {
  const v = parseFloat(icd);
  if (v <= 0.3) return 'Fast';
  if (v <= 0.65) return 'Balanced';
  return 'Precise';
}

module.exports = { applyICDFilter, getICDLabel };
