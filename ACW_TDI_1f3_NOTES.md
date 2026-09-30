# ACW ↔ TDI 1f3 — Risk Authority + Plain-Language HUD

1f3 is the last intended F-generation calibration pass before G unless TradingView screenshots expose a real semantic defect. It keeps the F1.2 MTF architecture and bridge transport unchanged.

## What changed

- **Exhaustion is now two-stage in ACW.** TDI exhaustion no longer forces every otherwise-good directional setup straight to WAIT. If the continuation is otherwise coherent, ACW keeps it at **WATCH** and labels the trend as **TIRED**. If exhaustion is corroborated by at least two maturity clues (cooling/pullback momentum, contracting/compressing MA core, non-fresh structure, or Near context no longer supporting), ACW escalates it to **TREND EXHAUSTED** and **WAIT • EXHAUST**.
- Exhaustion cannot manufacture a setup. The WATCH preservation requires same-direction ACW/TDI, supportive MA core, compatible structure, non-counter momentum, |confluence| >= 35 and confluence confidence >= 45.
- **Divergence remains secondary and freshness-weighted.** Fresh opposing divergence keeps the larger quality penalty and can downgrade READY → WATCH only when corroborated. Active/older divergence carries the smaller penalty and naturally expires through the existing TDI lifecycle.
- **Risk priority is explicit:** Exhaustion → Divergence → Flow opposition → Anchor opposition → reversal pressure.
- **Descriptive HUD language is more human-readable.** Examples include `UPTREND`, `DOWNTREND`, `FLOW SUPPORTS`, `FLOW OPPOSES`, `LONG CONTINUATION`, `SHORT CONTINUATION`, `MOMENTUM NOT READY`, and `MARKET COMPRESSED`.
- **Compact and Diagnostic HUDs remain available.** Compact stays dense/mobile-oriented; Diagnostic keeps technical values.
- TDI Descriptive HUD receives the same language cleanup. Divergence qualification and the already-added divergence lines/labels are unchanged.

## Preserved invariants

- Same F bridge payload, same magic, same 15 fields; F1.3 remains transport-compatible with F1/F1.1/F1.2.
- No new `request.security()` calls (TDI remains at four; ACW unchanged).
- Plot / plotshape / bgcolor / fill / alertcondition registration counts are unchanged.
- Squeeze remains a hard wait condition.
- No support/resistance subsystem was added; ROM remains the separate structure/levels animal.

## Suggested screenshot validation

Run the normal BTC / XAUUSD / HYPE stack across 1m, 3m, 5m, 7m, 15m, 45m, 1h, 2h, 4h and 6h. Pay special attention to three cases: a fresh trend that first enters exhaustion, a mature exhaustion after several cooling bars, and a fresh opposing divergence during an otherwise valid continuation. We want WATCH on the first, WAIT on the second, and a READY→WATCH downgrade only when the divergence has corroboration.

## Verification performed here

- `test_f1_3.py`: 7/7 tests passed.
- `verify_f1_3.py`: 47/47 static/regression checks passed.
- F bridge envelope remains below the IEEE-754 exact integer boundary (`2^53`).
- TradingView compilation/runtime is still the final external gate because the TradingView Pine compiler is not available in this environment.
