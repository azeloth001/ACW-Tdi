# ACW ∞ + TDI ∞ 1g — Implementation Notes

## What G adds

- ACW `Signal Personality`: **Selective / Balanced / Active**, default **Balanced**.
- Personality changes final promotion only; it does not redefine trend, structure, MA Core, TDI state, Near/Anchor, divergence, exhaustion, or bridge semantics.
- Confirmed-bar ACW lifecycle: **A↑/A↓ → ACTIVE → CAUTION → X / INV → re-arm**.
- Historical price markers for entry, exit and invalidation; caution marker is optional and OFF by default.
- Matching alert conditions driven by the exact lifecycle event booleans.
- Descriptive lifecycle HUD with signal age/reason plus compact mobile shorthand.
- Clearer Flow prose: directional support uses magnitude (`BULL/BEAR FLOW SUPPORTS N`) rather than a signed number that requires mental decoding.

## What G deliberately does not add

No automatic orders, no fixed TP/SL engine, no ROM-style support/resistance/Fibonacci subsystem, no new TDI market-state engine, and no new higher-timeframe requests.

## Local verification evidence

- **45/45** semantic/static regression tests pass on the final reviewed source.
- TDI F bridge encoder body equals F1.3.
- ACW F bridge decoder body equals F1.3.
- The wider frozen ACW F core from bridge decoding through F1.3 action construction is byte-for-byte identical to F1.3.
- `request.security()` call counts equal F1.3 (ACW 0, TDI 4).
- TDI has no Signal Personality input.
- Personality overlay does not mutate frozen market-state variables.
- Conservative source-call count including plots, lifecycle markers, alerts, bar/background coloring and fills remains below 64 in each script (ACW 43, TDI 38).
- Whole-branch final review found and fixed one pre-declaration `gReadiness` reference; its regression test went RED → GREEN before this final suite.

## Validation status

These are local semantic/static checks, **not a Pine compiler**. TradingView Pine v6 compile/runtime validation is still required using `G_RUNTIME_TEST_MATRIX.md`. G is **not production-frozen** until that runtime review and user acceptance are complete.
