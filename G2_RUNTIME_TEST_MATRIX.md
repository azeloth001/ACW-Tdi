# ACW ∞ 1g2 Market Phase — TradingView Runtime Matrix

Use normal candles. Keep **Signal Personality = Balanced** first. Connect ACW `TDI Bridge Bus` to unchanged `TDI ∞ 1g → TDI Bridge Bus`.

## What to record for every chart

| Check | What to observe |
|---|---|
| Market Phase | EARLY / MID / LATE / NEAR PRIOR HIGH/LOW |
| A? | Did it appear early enough to be useful, but only after real recovery evidence? |
| Graduation | Did same-direction A later confirm the A? without using the earlier A? price? |
| Expiry | Did failed A? disappear from state without an X/INV trade terminal? |
| Late guard | Did poor-location READY become WATCH only when weakness corroborated it? |
| Breakout exception | Did strong expanding continuation remain READY near/beyond prior extreme when not weakening? |
| Lifecycle | Existing A → ACTIVE → CAUTION → X/INV still coherent? |
| Visual | Labels readable at ~50% transparency, no price-number clutter, dotted confirmed connector clean? |
| Result | X/INV reports signed price move, not percent? |

## BTCUSDT museum stack

Test: **1m, 3m, 5m, 7m, 15m, 45m, 1h, 2h, 4h, 6h**.

Focus especially on:
- exhausted down-leg → early bullish recovery (`A?↑`) before the move is already mature;
- mature rebound approaching previous high → late-chase protection;
- clean breakout beyond prior high → ensure location alone does not block READY;
- compressed/choppy lower TFs → A? should remain scarce.

## GOLD / XAUUSD

Use representative lower/mid/higher sets from the prior F/G tests (for example 1m, 5m, 15m, 45m, 2h, 6h).

Focus on:
- divergence + phase interaction;
- `FLOW N/A` behavior;
- recovery after mature directional legs;
- no fake A? created by divergence alone.

## HYPE

Use representative lower/mid/higher sets from the prior F/G tests (for example 1m, 5m, 15m, 45m, 2h, 4h/6h).

Focus on:
- hostile Near+Anchor must block A?;
- counter-anchor situations;
- exhaustion-like stress cases;
- phase must not invent direction.

## Personality comparison after Balanced

Only after Balanced behavior is understood:

- **Selective:** fewer A?, earlier late-entry protection.
- **Active:** earlier A?, later tolerance for continuation.
- Market direction/structure itself should not change between personalities.

## Production-freeze criterion

G2 is ready to freeze only if BTC + GOLD + HYPE show **earlier useful recognition of obvious recovery phases without turning ACW into a noisy reversal picker**, while late-chase entries reduce and strong breakout cases still pass through when healthy.
