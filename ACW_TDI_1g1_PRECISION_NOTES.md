# ACW ∞ 1g1 Precision — lifecycle polish

## What changed

This is a presentation/bookkeeping refinement of ACW 1g. The G promotion/readiness engine is unchanged.

- `A↑ / A↓` labels are now small, dark, high-contrast and anchored to the **exact confirmed signal-candle close**.
- `X / INV` labels are anchored to the **exact confirmed terminal-candle close** and include direction-normalized result `%`.
- Completed lifecycles can draw a thin dotted **entry → exit** line. Default: ON.
- Optional live entry → current-price connector. Default: OFF.
- Descriptive HUD now shows exact active entry price and age.
- Descriptive HUD adds `LAST TRADE`, e.g. `X @85930.0 • +0.80% • 15b`.
- Compact HUD shows active entry price and age, or terminal result on the event bar.
- Lifecycle chart marks use `label.new()` rather than `plotshape()`, preserving the 1G plot-budget fix.

## Semantics

- Entry reference price = `close` of the confirmed bar that creates `A↑ / A↓`.
- Exit reference price = `close` of the confirmed bar that creates `X / INV`.
- `X` = lifecycle edge deteriorated enough to end the active setup. It can be a profit or loss exit.
- `INV` = the original directional thesis became invalidated. It is a semantic invalidation, not a pre-calculated fixed stop-loss.
- Result % is direction-normalized: long gains and short gains are positive; losses are negative.
- No TP or SL levels are projected in advance. The connector is a historical lifecycle trace, not a target forecast.

## Defaults

- Completed Trade Connectors: ON
- Active Trade Connector: OFF
- Entry Marks: ON
- Exit Marks: ON
- Invalidation Marks: ON
- Caution Marks: OFF

## Compatibility

- Use `TDI_1g.pine` unchanged.
- Reconnect ACW's source to `TDI ∞ 1g → TDI Bridge Bus` after replacing ACW if TradingView resets the source input.
- Signal Personality defaults remain unchanged; Balanced remains the default.

## Verification performed locally

- Precision regression suite: 9/9 pass.
- G promotion layer byte-identical to ACW 1g baseline.
- `request.security()` count unchanged.
- Alert set unchanged.
- Lifecycle plotshape calls: 8 → 0.
- Lightweight delimiter scan: pass.

TradingView compilation/runtime remains the final verification gate.
