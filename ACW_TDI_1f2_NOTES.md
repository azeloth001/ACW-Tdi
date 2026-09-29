# ACW ↔ TDI 1f2 — semantic/presentation cleanup

1f2 is a bounded cleanup of 1f1. It does **not** retune thresholds, change readiness/action rules, alter the F bridge format, or add new `request.security()` calls.

## Changes

- **Structure Freshness** now ages from the actual confirmed pivot bar (`bar_index[rightBars]`) instead of the later bar on which the pivot became confirmed. This removes the artificial `rightBars` freshness bonus.
- **ACW Descriptive Context** now includes readable automatic-ladder timeframe names, e.g. `NEAR 15m BULL 40 • ANCHOR 45m MIX -10`.
- **Mixed TDI Flow wording** is no longer shown as `NEUT +75`. When TDI Trend is MIX, ACW shows `FLOW +75 • UNPAIRED`; the flow value is real, but it has no trend direction to confirm/oppose yet.
- **TDI divergence lines** are increased from width 2 to width 3 for better phone visibility. Divergence qualification/lifecycle is unchanged.
- **Version headers/titles** now identify the pair as `1f2 / F1.2`.

## Preserved invariants

- F bridge payload and ACW decoder are byte-identical to 1f1.
- One hidden `TDI Bridge Bus` remains.
- Plot/shape/background/fill/alert registrations are unchanged.
- TDI still uses four `request.security()` calls; ACW adds none.
- SQUEEZE/EXHAUST hard-veto logic, CHOP soft semantics, Quality penalties, action/readiness rules, and all thresholds are unchanged.

## Context-label note

ACW does not receive timeframe IDs through the packed bus, so its new timeframe labels mirror the **automatic** Near/Anchor ladder. When TDI is set to **Manual Context Selection**, the TDI HUD remains the authoritative place to read the selected manual timeframe names. Scores/states transported to ACW remain correct either way.

## Verification

- `test_f1_2.py`: 6/6 tests passed.
- `verify_f1_2.py`: 17/17 static/regression checks passed.
- Bridge envelope remains below the IEEE-754 exact integer boundary (`2^53`).
- TradingView compile/runtime remains the final gate.
