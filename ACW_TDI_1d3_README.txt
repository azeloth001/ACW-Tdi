ACW ↔ TDI 1d3 — Semantic Bridge Calibration

PAIR
- ACW_1d3.pine
- TDI_1d3.pine

SETUP
1. Add TDI 1d3 to TradingView.
2. Add ACW 1d3.
3. In ACW > 06 • TDI Link / Confluence, select:
   TDI Bridge Bus -> TDI ∞ 1d3 -> TDI Bridge Bus
4. Start with TDI Integration = Advisory.

WHAT CHANGED
- One-link bridge remains one hidden plot.
- Bridge now also carries TDI Regime and persistent Ready direction.
- Raw TDI Fusion alone can no longer create ALIGNED/READY.
- TDI Bias or TDI Ready establishes TDI direction.
- READY requires TDI's own Ready state in the same direction.
- CHOP/SQUEEZE remain WAIT timing states.
- EXHAUSTION blocks READY and premium synchronized diamonds.
- Recovery/Pullback now explicitly show / EXH when TDI is exhausted.
- Premium LONG/SHORT SYNC requires TDI readiness; Confirm mode still additionally requires the sparse TDI event signal.
- Underlying ACW weights and TDI engine math are unchanged.

TARGETED SCREENSHOT FIXES
- 45m: TDI Fusion around +19 with MIXED bias + WAIT can no longer become ACW ALIGNED/READY/LONG SYNC merely from raw Fusion.
- 4h: mild positive TDI with MIXED bias stays ACW LEADS / WAIT TIMING unless TDI itself becomes directional/ready.
- 6h: bullish recovery with TDI EXHAUSTION becomes RECOVERY ↑ / EXH with EXHAUST timing, not READY.

LOCAL VERIFICATION
- 9/9 regression tests passed.
- 5,000 randomized bridge encode/decode round-trips passed.
- Maximum packed bus integer: 722,396,810,161 (< 2^53).
- TDI plot-producing call counts did not increase vs 1d2.
- Pine parser-risk and delimiter static checks passed.

FINAL GATE
TradingView Pine compiler + visual/runtime screenshots.
