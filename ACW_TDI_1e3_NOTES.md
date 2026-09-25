# ACW + TDI 1e3 — Exhaustion Semantic Veto

## Why 1e3 exists
HYPE 3D exposed a semantic mismatch in 1e2: TDI ACTION could show `EXHAUST ↑/↓` while TDI REGIME still encoded `CHOP`. ACW receives REGIME through the bridge, not the ACTION label, so ACW could miss the exhaustion warning and promote a context-assisted continuation to `LONG CONT` / `SHORT CONT`.

## Root cause
TDI action priority was:
`SQUEEZE → EXHAUSTION → READY/TREND → CHOP → WAIT`

but TDI regime priority was:
`SQUEEZE → CHOP → EXHAUSTION → ...`

The same bar could therefore say ACTION=`EXHAUST ↑` while the bridge sent REGIME=`CHOP`.

## 1e3 change
TDI regime priority is aligned to:
`SQUEEZE → EXHAUSTION → CHOP → EXPANSION → TREND → TRANSITION`

ACW already had `not tdiExhaustion` guards for both normal readiness and context-assisted continuation, so no threshold, scoring, bridge-format, or continuation logic change was required.

## Expected HYPE 3D behavior
A bar that previously showed TDI `EXHAUST ↑` + REGIME `CHOP` while ACW showed `READY • CONT / LONG CONT` should now reach ACW as EXHAUSTION and be blocked from continuation promotion. ACW may remain aligned/watch, but should not display `LONG CONT` / `SHORT CONT` while exhaustion is active.

## Unchanged
- 1e2 continuation thresholds
- medium WATCH TREND thresholds
- ACW context-assisted continuation requirements
- bridge field layout and magic
- plot/shape/fill/alert budget
- visuals

## Pairing
Use `TDI 1e3 ↔ ACW 1e3` for clean version tracking. The bridge format itself remains unchanged from 1e1/1e2.

TradingView compile/runtime remains the final validation gate.
