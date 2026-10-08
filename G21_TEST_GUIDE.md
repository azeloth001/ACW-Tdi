# ACW 1g21 — Turning Pressure experiment

Status: local gate tests and source-isolation checks passed. TradingView compilation and chart replay NOT performed. This is a research candidate, not a production promotion or a demonstrated improvement in profitability.

## Install and first test

1. Keep ACW 1g2 available as the control. Add `ACW_1g21_Turning_Pressure.pine` as a separate indicator.
2. Keep the existing TDI 1g companion. Select its `TDI Bridge Bus` in the new ACW instance. Normal candles, Balanced personality, Advisory integration; use the same symbol/feed and settings as the control.
3. Start with `09 • G2.1 Turning Pressure Experiment → Turning Pressure mode = Observe` (default). This changes the experimental phase readout but leaves the original A? event path in effect.
4. Use `Early A?` to test the new early-observation path. `Off` restores original G2 phase/A? behavior. Normal A/X/INV, entry/exit prices and completed results must agree across modes.

For the first screenshots, use Descriptive HUD. Diagnostic adds the original G2 phase beside the experimental phase, plus normalized velocity, acceleration, Z-score and recovery fraction. The TURN PROBE row says what blocks qualification.

## Small first round — no full museum rerun yet

| Chart | Question | Pass/fail evidence |
|---|---|---|
| BTCUSDT 45m | Does the old upward phase survive a confirmed break below its anchor? | Observe should switch to a clearly marked developing bearish leg after the price/MA gate. Only qualified recovery becomes EARLY RECOVERY ↑ • PROBE. A bullish label is not required on the screenshot's final candle. |
| BTCUSDT 1h | Can improving bearish momentum support recovery before a formal pivot/crossover? | Replay successive closed candles; record first qualifying probe, first experimental A?, first normal A (if any), and failed/expired observations. |
| BTCUSDT 2h | Is the late-entry guard preserved? | Compare the known WATCH • NEAR PRIOR LOW case under identical settings. |
| BTCUSDT 1m and 3m | Does the probe become noisy in chop? | Replay the same fixed interval in Off and Early A?; count additional A?, repeated marks around one extreme, and recoveries that fail. Include failures, not only attractive turns. |

Send 45m and 1h screenshots first, preferably the first closed bar marked QUALIFIED/A? and several bars later. Include the TURN PROBE row. If compilation fails, send the exact compiler message and highlighted line before spending time on chart tests.

If this first round behaves sensibly, expand to bearish turns, a clean breakout, XAUUSD with missing flow, HYPE with hostile Near+Anchor, and the original wider timeframe matrix. Freeze only after forward/replay evidence; screenshots alone do not establish an edge.

## What the code investigation found

G2 assigns `g2PrimaryDir` from the last confirmed swing kind. A confirmed low implies an upward developing leg. If price subsequently falls through that low before another alternating swing is confirmed, the direction can remain upward and the running high can still refer to an earlier bounce. The A? candidate is its opposite, so a momentum improvement alone cannot repair the stale directional reference.

The candidate adds a separate provisional reference after a confirmed close breaches that anchor by 0.25 ATR and the existing MA Core agrees with the breach. This reference tracks the new extreme until a new confirmed anchor arrives or price invalidates the provisional leg by reclaiming its origin. It never rewrites confirmed swing structure or the original G2 guard's geometry. `DEV LEG` explicitly identifies this provisional phase.

The supplied 45m screenshot is consistent with this mechanism; its exact historical bar state has not been reconstructed from OHLC data. The 2h screenshot explicitly shows the late guard. Other WAIT screenshots may be blocked by existing timing/context rules, so they are not all evidence of incremental guard benefit.

## Mathematics retained, with limits

- Three fixed-length EMA MACD branches: fast uses roughly half the existing ACW lengths; middle reuses ACW's histogram; slow uses roughly 1.5 times the lengths. GMACD's +1/+2 parameter changes do not guarantee fast-to-slow event order, so no such ordering is assumed.
- Smoothed residual velocity and its acceleration. Raw residual differences are calculated BEFORE ATR normalization, preventing denominator changes alone from manufacturing a directional derivative.
- Average absolute residual magnitude measures contraction. It is an amplitude measure, not statistical independence or proof that a trend has lost coherence.
- Raw middle MACD Z-score, 50-bar window, with an 8-bar extreme memory and release toward zero. Z-score release is supporting evidence; it cannot trigger alone, and changing mean/variance can affect it.
- Two consecutive fast-velocity signs, middle-velocity agreement, and a minimum velocity floor. Positive curvature or Z release is needed, together with contraction or release.
- Mature leg, bounded ATR/fraction recovery, and actual price displacement/reclaim are mandatory. All MACD-derived components collectively form ONE momentum evidence family; they are not counted as independent votes.

Starting thresholds are engineering hypotheses, not fitted or validated market calibration. Balanced velocity floor is 0.003 ATR/bar; fast residual may remain on the old side or cross slightly (up to 0.08 ATR on the candidate side). Existing G2 recovery thresholds are reused. Selective additionally needs clean context support or supporting flow. Mirror rules apply to bearish recovery.

No GMACD visuals, nine-timeframe matrix, RSI/Stoch/CCI, Fibonacci, fractals or new security requests were imported. This experiment does not establish that any derivative predicts price.

## Modes and lifecycle details

- Off: original G2 behavior, apart from version/diagnostic presentation and extra background calculations.
- Observe: confirmed experimental phase/probe display; original A? remains unchanged. If an original A? is active it still takes precedence in the main phase row; inspect TURN PROBE/Diagnostic for the experiment.
- Early A?: original early path remains available except when it relies on the invalidated shadow reference; the qualified probe can start an A?. Repeated experimental observations in the same extreme area are suppressed; a new confirmed-anchor episode or a material new extreme can rearm.
- Existing A? expiry and A graduation are retained. Experimental A? uses its own observed extreme for failure checks. A on the same bar suppresses A?; confirmed A always owns its own close, never the earlier probe price.
- A? history labels remain on the chart when their active state expires. Expiry does not create an X/INV trade terminal.
- As in original G2, linked contexts remain relevant to A? even if integration is Off, and decoded candidate-direction hard risk remains blocking even with Force Unlinked. Use Advisory for the comparison. This inherited behavior was deliberately preserved, not redesigned here.
- Turning Pressure cannot create a normal A, change an X/INV, or alter trade results. A useful early observation can therefore appear while ACTION still says WAIT.

## Verification and reproducibility

Run from this package directory:

```bash
python3 -m unittest discover -s tests -v
python3 verify_invariants.py
```

Ten tests evaluate the actual pure Pine gate bodies on hand-checked scalar fixtures through a limited Python evaluator. They cover mirrored turns, contraction without turning, raw extremes, isolated twitches, recovery limits, risk/context blocks and episode rearming. The tests were observed failing before their corresponding implementation/fixes. They do NOT execute the complete Pine state machine, EMA initialization, live-bar rollback, bridge synchronization or TradingView compilation.

The source audit confirms byte-identical bridge decoder, original G2 phase geometry/thresholds, late guard and confirmed lifecycle, and alert registrations. Security requests remain 0; plot/plotshape/alertcondition counts are unchanged. Delimiter checking is only a static sanity check. A separate code review found and prompted fixes to episode rearming and TDI gate consistency.

Frozen TDI SHA256:
`17c3a59a392d021178912be98924e765bd97950443fb430ba26d64e7a32598e6`

GitHub history inspected: https://github.com/azeloth001/ACW-Tdi — default branch currently tracks 1d2. The supplied 1g2/1g handoff is the experiment's baseline. No GitHub files were modified.

Pine implementation constraints checked against official documentation:
- https://www.tradingview.com/pine-script-docs/language/type-system/
- https://www.tradingview.com/pine-script-docs/language/execution-model/

All newly added series calculations run each bar; experimental state/display commits use confirmed bars. Original live HUD/plot behavior is retained elsewhere. Reload/replay stability still requires TradingView testing.
