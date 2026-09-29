# ACW ∞ + TDI ∞ 1f1 — Semantic Correction Pass

## Purpose
1f1 is a bounded correction pass on the F architecture. It does not add a new engine or retune the core E/F thresholds. It corrects live semantic issues exposed by the first BTC F screenshots and improves divergence visibility.

## ACW 1f1 corrections
- **Structure freshness** now resets only on a newly confirmed alternating swing leg. Same-side pivot replacement can refine the current leg, but it no longer makes old structure look freshly confirmed.
- **Divergence is always visible in the RISK row** while fresh/active, even when there is no current action direction. Divergence only penalizes Quality/readiness when it actually opposes the candidate direction, preserving the warning-vs-direction separation.
- **Descriptive context is descriptive:** e.g. `NEAR BULL 30.0 • ANCHOR MIX -10.0`. Compact HUD keeps the short arrow form.
- **CHOP is soft in F:** a coherent local price/MA/TDI state can be rescued from legacy `WAIT` to **WATCH only**. This cannot manufacture READY.
- **SQUEEZE and same-direction EXHAUSTION remain hard action blockers.**
- **WAIT reasons are preserved**: `WAIT • SQUEEZE`, `WAIT • EXHAUST`, `WAIT • CHOP`, `WAIT • CONTEXT`, `WAIT • TIMING`, `WAIT • CONFLICT`, etc.

## TDI 1f1 corrections
- Qualified divergence visualization is **ON by default**.
- Every qualified pivot divergence draws a visible dashed line directly on the TDI oscillator pane.
- Divergence lines are stronger (full-color, width 2); `DIV ▲/▼` labels remain spaced so the pane does not become label soup.
- Descriptive Near/Anchor rows now use readable timeframe labels and spell out `CONFIRMED` / `DEVELOPING` instead of `C` / `D`.

## Deliberately unchanged
- TDI Trend Carrier, Momentum, Flow, readiness thresholds and regime calculations.
- Near/Anchor context calculation and confirmed-context bridge authority.
- ACW legacy E confluence/action block.
- F packed bridge format and precision; **1f1 is wire-compatible with 1f**.
- Plot/plotshape/bgcolor/fill/alert registration counts.

## Local verification
- 15 semantic/model tests passed.
- 35 Pine-specific static/regression checks passed.
- F bus maximum envelope remains `5,958,740,783,038,419`, below IEEE-754 exact integer limit `2^53 = 9,007,199,254,740,992`.
- ACW legacy E confluence/action block is byte-identical to 1f.
- TDI bridge math and ACW decoder are byte-identical to 1f.
- `request.security()` count is unchanged.

## TradingView gate
This environment cannot run TradingView's Pine compiler. Compile/runtime behavior in TradingView remains the final gate.

### First live checks
1. Connect ACW 1f1 to the **TDI 1f1 → TDI Bridge Bus** source.
2. Keep both HUDs on **Descriptive + Tiny** first.
3. Confirm TDI draws a visible line when `BULL/BEAR DIV` is reported.
4. Revisit BTC 7m/15m-like cases: coherent CHOP states may now become `WATCH`, never READY merely because CHOP was softened.
5. Confirm squeeze/exhaust cases still read `WAIT • SQUEEZE` / `WAIT • EXHAUST`.
6. Check that higher-TF structure now has a realistic chance to progress from FRESH → MATURE → AGING instead of being refreshed by same-side swing replacement.
