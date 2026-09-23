# ACW + TDI 1e1 — Dual Readiness Calibration

## What changed

1e1 keeps the E Trend / Momentum / Flow separation and adds a second TDI readiness archetype.

- `LONG` / `SHORT` = legacy impulse readiness (fresh, high-momentum gate).
- `LONG TREND` / `SHORT TREND` = established-trend continuation readiness.
- ACW receives the readiness subtype through the same single `TDI Bridge Bus` source.
- ACW displays continuation timing as `READY • TREND` and, when ACW confluence is strong enough, `LONG CONT` / `SHORT CONT`.

## Continuation gate

Continuation readiness requires all of the following:

- Price Core direction is established and strong (`>= +55` or `<= -55`).
- Price Persistence and Trend Geometry agree with the carrier direction.
- Regime is not SQUEEZE, CHOP, or EXHAUSTION.
- Momentum is not COUNTER.
- Fusion retains modest same-direction pressure (`>= +12` bullish / `<= -12` bearish).

OBV Flow does not grant continuation readiness. Missing volume therefore does not disable the new path.

## Important pairing rule

1e1 uses a new bridge magic and five-state readiness encoding. Pair only:

- `TDI_1e1.pine` ↔ `ACW_1e1.pine`

Do not mix 1e and 1e1 buses. The new magic intentionally makes cross-version links invalid instead of silently decoding the wrong semantics.

## Oil test expectation

The WTI screenshots that motivated 1e1 should not produce SHORT on every timeframe. The intended pattern is:

- weak carrier / CHOP / SQUEEZE / structural contradiction → WAIT/WATCH remains valid;
- strong established bear carrier + bearish geometry/persistence + non-chop regime + still-negative momentum → `SHORT TREND`;
- ACW only promotes that to `SHORT CONT` when its own direction/confluence is sufficiently supportive.

TradingView compile/runtime remains the final Pine v6 gate.
