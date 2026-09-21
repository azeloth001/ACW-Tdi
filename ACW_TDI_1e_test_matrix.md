# ACW/TDI 1e TradingView Test Matrix

## Compiler gate
- TDI 1e compiles in TradingView Pine v6.
- ACW 1e compiles in TradingView Pine v6.
- No 64-plot-count runtime rejection.
- One TDI Bridge Bus is selectable from ACW.

## Link gate
- Correct TDI 1e bus shows LINKED.
- Unlinked/default source safely falls back.
- 1d3 bus source is rejected as invalid E bridge.

## BTCUSDT
- 1m / 3m / 5m / 7m / 15m.
- 45m / 1h / 2h / 4h / 6h sanity views.
- Revisit the 81k→86k directional day: Trend should remain BULL through oscillator cooling where Price Core persists.

## ETHUSDT
- 1m / 3m / 5m / 7m / 15m.
- 45m sanity view.

## Behavior coverage
- strong trend
- healthy consolidation
- pullback
- sideways chop
- squeeze
- squeeze release
- exhaustion
- one-candle spike
- real reversal
- flow confirmation
- flow opposition
- weak/missing volume if available on a test symbol

## Visual gate
- bullish zigzag visible on light background without neon glare
- ACW colored HUD cells retain white readable values
- TDI TREND / MOMENTUM / FLOW rows readable at Tiny size
- candle direction does not flip solely from temporary opposite Momentum inside persistent Trend

## Freeze gate
- sustained direction can coexist with COOLING/PULLBACK momentum
- real reversals eventually change Trend State
- Flow never creates direction or READY
- synchronized signal still requires Timing Ready
- BTC and ETH both coherent before 1e is called stable
