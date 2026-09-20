# ACW ↔ TDI

Shared Pine Script v6 development repository for the matched ACW/TDI indicator pair.

- **ACW** — structure, trend environment, pressure, and chart atmosphere.
- **TDI** — timing, momentum quality, regime transition, and execution context.

## Current tracked generation

- ACW 1d2
- TDI 1d2

The shared letter identifies the compatible generation. Numeric suffixes such as 1d1/1d2 are local calibration or fix steps within that generation. The next major shared evolution moves both indicators to the next letter.

## TradingView setup

1. Add **TDI 1d2**.
2. Add **ACW 1d2**.
3. In ACW open **06 • TDI Link / Confluence**.
4. Set **TDI Bridge Bus** to **TDI 1d2 → TDI Bridge Bus**.
5. Start with **TDI Integration = Advisory** during calibration.

## Repository layout

- `ACW/` — ACW source + changelog
- `TDI/` — TDI source + changelog
- `docs/ACW_TDI_RULEBOOK.md` — paired system interpretation
- `docs/VERSION_HISTORY.md` — version lineage
- `docs/TEST_LOG.md` — TradingView test observations

GitHub is the durable source/history. Chat remains the active lab for screenshots, calibration, and direct `.pine` downloads.
