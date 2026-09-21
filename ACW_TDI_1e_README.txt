ACW + TDI 1e — E Generation Release Candidate
===============================================

Files
-----
TDI_1e.pine
ACW_1e.pine
ACW_TDI_1e_test_matrix.md

What E changes
--------------
- TDI Trend is now a persistent local price-domain carrier, separate from RSI/Fusion momentum.
- Price Core combines directional persistence + local trend geometry.
- OBV-style Flow uses ~30-bar memory and can strengthen/weaken trust, but cannot choose trend direction or create READY by itself.
- Momentum can COOL / PULLBACK / RECOVER while Trend remains BULL or BEAR.
- ACW gets Trend / Momentum / Flow / Timing separately through one hidden bridge bus.
- ACW bullish zigzag uses darker emerald/teal (#00A878) for light backgrounds.
- ACW HUD keeps colored cells but uses white value text for readability.

TradingView setup
-----------------
1. Add TDI_1e.pine and confirm it compiles/runs first.
2. Add ACW_1e.pine and confirm it compiles/runs.
3. Open ACW settings -> TDI Link / Confluence -> TDI Bridge Bus.
4. Select: TDI ∞ 1e -> TDI Bridge Bus.
5. Do NOT connect a 1d3 bridge to ACW 1e; E intentionally uses a new incompatible bus contract.

First tests
-----------
- BTCUSDT: 1m, 3m, 5m, 7m, 15m; then 45m/1h sanity.
- ETHUSDT: 3m, 5m, 15m first.
- Look specifically for: BULL/BEAR Trend persisting while Momentum says COOLING/PULLBACK instead of collapsing immediately to MIXED.
- Check Flow CONFIRM / OPPOSE behavior and that Flow never creates direction on its own.
- Check darker bullish zigzag and white ACW HUD values on your light background.

Local verification
------------------
The local reference/static suite passed 37/37 tests. E did not increase the counted render/alert-call budget versus 1d3 in either script. TradingView Pine v6 compilation/runtime remains the final validation gate.
