# ACW ∞ + TDI ∞ 1e4 Core Sanitation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce ACW 1e4 + TDI 1e4 as a mathematically/semantically sanitized E-core baseline by removing exact MACD Council double-counting, correcting misleading QUALITY/Context-TF presentation, cleaning proven dead code, and preserving the 1e3 bridge and E trading semantics.

**Architecture:** 1e3 remains the immutable control. 1e4 changes only demonstrated sanitation defects: ACW's Council becomes eight unique equal-weight binary observations, while TDI/ACW presentation becomes semantically truthful. No F-generation intelligence is introduced; the TDI bridge, Trend/Momentum/Flow logic, continuation thresholds, exhaustion veto, MAMA formula, ZigZag logic, and 45/35/20 ACW weights remain intact.

**Tech Stack:** Pine Script v6; Python 3 static/regression tests; ZIP packaging; TradingView as final compile/runtime gate.

**Spec:** `docs/superpowers/specs/2026-09-28-acw-tdi-1e4-core-sanitation-design.md`

## Global Constraints

- Baseline sources are `/mnt/data/ACW_1e3.pine` and `/mnt/data/TDI_1e3.pine`; never overwrite them.
- Candidate outputs are `/mnt/data/ACW_1e4.pine` and `/mnt/data/TDI_1e4.pine`.
- Keep the TDI E bus magic, radices, channel order, quantization, and payload limits unchanged.
- Keep TDI Price Core / Trend Carrier, Momentum, Flow, squeeze/chop/exhaustion, continuation thresholds, 1e3 exhaustion veto, and signal semantics unchanged.
- Keep ACW MAMA/FAMA formula and default fusion weights `45 / 35 / 20` unchanged.
- Keep ZigZag pivot confirmation, stored `lastHighTime`/`lastLowTime`, and `swingEvent` intact for F.
- No MA Core expansion/contraction, structure freshness weighting, adaptive MTF ladder, evidence-family weighting, ADX, or Signal Audit logic in 1e4.
- Parser-safe Pine style: avoid multiline ternary hazards and do not introduce dynamic series lengths.
- Local verification is static/semantic only; TradingView compile/runtime remains the final gate.

## Review Focus

1. **Council scale after de-duplication:** all eight unique votes must still span exactly `-100…+100` in 25-point increments; no accidental 80-point or 125-point range.
2. **Context-TF relation on unusual charts/timeframes:** `↑ / = / ↓` must be shown only when timeframe durations are comparable; otherwise show neutral `CTX <tf>` rather than guessing.
3. **Bridge wire compatibility:** changing QUALITY labels must not alter `eConfidenceQ`, bus magic, radix multipliers, ready/event/regime coding, or the hidden plot title.
4. **E-behavior preservation:** long/short impulse, trend continuation, medium trend watch, regime priority, and exhaustion veto expressions must remain textually/semantically identical to 1e3.
5. **Pine budget/parser safety:** plot/plotshape/fill/alertcondition counts must not increase, and the candidate must pass the existing parser-risk/static scans before packaging.

---

### Task 1: Pin 1e3 invariants with a sanitation regression harness

**Files:**
- Create: `/mnt/data/tests/test_1e4_core_sanitation.py`
- Read-only baseline: `/mnt/data/ACW_1e3.pine`
- Read-only baseline: `/mnt/data/TDI_1e3.pine`

**Interfaces:**
- Consumes: exact 1e3 Pine source text.
- Produces: reusable Python assertions/helpers for source expressions, occurrence counts, Pine render-budget counts, and protected E/bridge invariants.

- [ ] **Step 1: Write baseline tests that describe the intended 1e4 delta before candidate files exist**

Create tests with these exact expectations:

```python
def test_candidate_files_exist():
    assert ACW_1E4.exists()
    assert TDI_1E4.exists()


def test_acw_council_has_eight_unique_votes_and_no_exact_duplicates():
    src = ACW_1E4.read_text()
    assert "f_vote(macdLine > 0.0)" not in src
    assert "f_vote(macdHist > 0.0)" not in src
    for expr in UNIQUE_VOTE_EXPRESSIONS:
        assert expr in src
    assert "macdVotes * 12.5" in src


def test_bridge_constants_and_packing_match_1e3():
    # Extract TDI_E_BUS_MAGIC and ePayload packing lines from both versions.
    assert protected_bridge_block(TDI_1E4) == protected_bridge_block(TDI_1E3)
    assert protected_bridge_decoder_block(ACW_1E4) == protected_bridge_decoder_block(ACW_1E3)


def test_protected_tdi_e_logic_matches_1e3():
    for symbol in PROTECTED_TDI_EXPRESSIONS:
        assert expression_for(TDI_1E4, symbol) == expression_for(TDI_1E3, symbol)
```

`UNIQUE_VOTE_EXPRESSIONS` must contain exactly:
`fastMA > slowMA`, `ta.change(fastMA) > 0.0`, `ta.change(slowMA) > 0.0`, `ta.change(macdLine) > 0.0`, `macdLine > macdSignal`, `ta.change(macdHist) > 0.0`, `macdSignal > 0.0`, `ta.change(macdSignal) > 0.0`.

`PROTECTED_TDI_EXPRESSIONS` must pin: `longReady`, `shortReady`, `trendContinuationLong`, `trendContinuationShort`, `mediumTrendWatchLong`, `mediumTrendWatchShort`, `regime`, `actionName`, `eRegimeQ`, `eReadyQ`, and `eSignalQ`.

- [ ] **Step 2: Add semantic Council-scale tests independent of Pine text**

```python
def test_eight_vote_scale_is_symmetric_and_bounded():
    scores = [max(-100.0, min(100.0, vote_sum * 12.5)) for vote_sum in range(-8, 9, 2)]
    assert scores == [-100, -75, -50, -25, 0, 25, 50, 75, 100]
```

- [ ] **Step 3: Add render-budget and parser-risk helpers**

Count `plot(`, `plotshape(`, `fill(`, `bgcolor(`, and `alertcondition(` for each 1e3/1e4 pair; candidate counts must be `<=` baseline counts. Add scans that fail on known risky formatting patterns used in earlier E failures (assignment followed by an indented expression-only continuation and multiline chained ternary introduced by this patch).

- [ ] **Step 4: Run the harness and verify RED**

Run:

```bash
python -m unittest /mnt/data/tests/test_1e4_core_sanitation.py -v
```

Expected: FAIL because `/mnt/data/ACW_1e4.pine` and `/mnt/data/TDI_1e4.pine` do not yet exist.

- [ ] **Step 5: Checkpoint**

Preserve the failing test harness before creating candidates. If executing inside a git worktree, commit it as `test: pin 1e4 sanitation invariants`.

---

### Task 2: Sanitize ACW Council, QUALITY semantics, identity, and proven dead code

**Files:**
- Create from baseline: `/mnt/data/ACW_1e4.pine`
- Test: `/mnt/data/tests/test_1e4_core_sanitation.py`

**Interfaces:**
- Consumes: ACW 1e3 architecture and unchanged TDI E bridge format.
- Produces: ACW 1e4 with an eight-observation Council whose `macdScore` remains `-100…+100`, truthful QUALITY HUD labels, 1e4 identity, and behavior-neutral dead-code removal.

- [ ] **Step 1: Extend tests for the exact ACW user-visible and dead-code requirements**

Add assertions that ACW 1e4:
- contains `title = "ACW ∞ Spectral Fusion PRO 1e4"` and `shorttitle = "ACW ∞ 1e4"`;
- describes the architecture as an `8-vote` Council;
- uses bridge tooltip text pointing to `TDI ∞ 1e4 → TDI Bridge Bus`;
- contains HUD label `QUALITY` and does not contain HUD label `CONFIDENCE`;
- does not append `%` to `confidence` or `confluenceConfidence` HUD formatting;
- removes `tdiImpulseReady`, `biasName`, and `dashDetail`;
- preserves `lastHighTime`, `lastLowTime`, and `swingEvent`;
- preserves default weights exactly (`mamaWeight=45`, `macdWeight=35`, `structureWeight=20`, matching their source declarations).

- [ ] **Step 2: Run ACW-specific tests and verify RED**

Run the ACW test subset by name. Expected: FAIL against the not-yet-created/unchanged candidate.

- [ ] **Step 3: Copy 1e3 to 1e4 and implement the minimal Council correction**

In `/mnt/data/ACW_1e4.pine`:
- keep `vote1`, `vote2`, `vote3` as stack/fast-slope/slow-slope;
- remove the `macdLine > 0.0` duplicate;
- keep MACD acceleration, MACD-vs-signal, histogram acceleration, signal-line position, and signal-line slope as the remaining five unique votes;
- make the summed vote count eight observations;
- set `macdScore = f_clamp(macdVotes * 12.5, -100.0, 100.0)`.

Do not add replacement weighting or new ribbon geometry.

- [ ] **Step 4: Apply ACW semantic sanitation only**

Update 1e4 title/header/comments and bridge tooltip. Change both linked and native dashboard row labels from `CONFIDENCE` to `QUALITY`; render the same numeric values with `str.tostring(..., "#.0")` and no percent suffix. Internal `confidence`, `tdiConfidence`, and `confluenceConfidence` variables stay named and calculated as before.

- [ ] **Step 5: Remove only ACW variables proven dead in 1e3**

Delete `tdiImpulseReady`, `biasName`, and `dashDetail`; do not delete swing timestamps or `swingEvent`.

- [ ] **Step 6: Run ACW sanitation tests and verify GREEN**

Run the ACW subset plus Council semantic-scale test. Expected: PASS.

- [ ] **Step 7: Checkpoint**

If executing inside git, commit as `refactor: sanitize ACW 1e4 council and quality semantics`.

---

### Task 3: Sanitize TDI Context-TF semantics, QUALITY presentation, identity, and proven dead code

**Files:**
- Create from baseline: `/mnt/data/TDI_1e4.pine`
- Test: `/mnt/data/tests/test_1e4_core_sanitation.py`

**Interfaces:**
- Consumes: unchanged TDI 1e3 decision engine and E bridge encoding.
- Produces: TDI 1e4 with neutral Context-TF labeling, explicit `↑ / = / ↓` relation when safely comparable, truthful QUALITY presentation, and no decision-path changes.

- [ ] **Step 1: Extend tests for TDI user-visible/context/dead-code requirements**

Assert TDI 1e4:
- contains title `TDI ∞ Adaptive Spectral Engine 1e4 — Fusion`, shorttitle `TDI ∞ 1e4`, and HUD header `∞ TDI E4`;
- input labels contain `Context TF` and `Context Mode`, and no user-visible `Higher-TF Context` / `HTF Mode` remains;
- HUD row uses `CTX ` rather than `HTF `;
- contains relation tokens for `↑`, `=`, `↓` plus a neutral fallback;
- HUD label is `QUALITY`, with no `%` appended to `confidence`;
- removes `biasBull`, `biasBear`, `fastBasisUp`, `fastBasisDn`, `longTimingReady`, `shortTimingReady`, and `inExtOS`;
- preserves the exact bridge packing constants and protected E expressions.

- [ ] **Step 2: Add pure-Python relation tests for the intended UI rule**

```python
def relation(chart_s, context_s):
    if chart_s is None or context_s is None:
        return ""
    return "↑" if context_s > chart_s else "↓" if context_s < chart_s else "="


def test_context_relation():
    assert relation(60, 3600) == "↑"
    assert relation(3600, 3600) == "="
    assert relation(14400, 3600) == "↓"
    assert relation(None, 3600) == ""
```

- [ ] **Step 3: Run TDI-specific tests and verify RED**

Expected: FAIL before TDI 1e4 implementation.

- [ ] **Step 4: Copy 1e3 to 1e4 and rename display/input semantics without changing request behavior**

Keep the existing timeframe input value and Confirmed/Developing `request.security()` behavior, but change user-facing labels/tooltips to Context terminology. Internal `htf*` variable names may remain to minimize churn.

- [ ] **Step 5: Add parser-safe Context-TF relation calculation**

Use Pine's duration conversion only for display:

```pine
float chartTfSeconds = timeframe.in_seconds()
float contextTfSeconds = timeframe.in_seconds(htfTf)
bool contextTfComparable = not na(chartTfSeconds) and not na(contextTfSeconds)
string contextRelation = not contextTfComparable ? "" : contextTfSeconds > chartTfSeconds ? " ↑" : contextTfSeconds < chartTfSeconds ? " ↓" : " ="
```

If a chart type/timeframe cannot yield comparable seconds, leave `contextRelation` empty. Use it only in the HUD label: `"CTX " + htfTf + contextRelation`. Do not feed these values into `fusion`, `confidence`, `regime`, readiness, action, or bridge packing.

- [ ] **Step 6: Apply TDI QUALITY and identity sanitation**

Update header/title/HUD to 1e4/E4. Change `CONF` to `QUALITY`; display the existing `confidence` numeric value without `%`. Do not change `confidenceRaw`, penalties, floors, visual alpha formulas, or bridge quantization.

- [ ] **Step 7: Remove only TDI variables proven single-reference/dead in 1e3**

Delete `biasBull`, `biasBear`, `fastBasisUp`, `fastBasisDn`, `longTimingReady`, `shortTimingReady`, and `inExtOS`. Confirm no references remain.

- [ ] **Step 8: Run TDI/context tests and verify GREEN**

Expected: PASS for TDI-specific tests, protected-E-expression checks, and bridge checks.

- [ ] **Step 9: Checkpoint**

If executing inside git, commit as `refactor: sanitize TDI 1e4 context and quality semantics`.

---

### Task 4: Full regression gate, artifact notes, and package

**Files:**
- Verify: `/mnt/data/ACW_1e4.pine`
- Verify: `/mnt/data/TDI_1e4.pine`
- Create: `/mnt/data/ACW_TDI_1e4_NOTES.md`
- Create: `/mnt/data/ACW_TDI_1e4_pair.zip`
- Test: `/mnt/data/tests/test_1e4_core_sanitation.py`

**Interfaces:**
- Consumes: completed ACW/TDI 1e4 candidates.
- Produces: verified 1e4 pair ready for TradingView compile and side-by-side 1e3 benchmark testing.

- [ ] **Step 1: Run the complete sanitation suite fresh**

```bash
python -m unittest /mnt/data/tests/test_1e4_core_sanitation.py -v
```

Expected: all tests PASS with zero failures/errors.

- [ ] **Step 2: Run fresh structural diff checks against 1e3**

Generate a focused diff and verify every changed hunk belongs to one of these allowed categories only: Council de-dup/12.5 scale, 1e4 identity/comments/tooltip, QUALITY display semantics, Context-TF presentation/relation, or listed dead-code deletion. Any other decision-engine hunk is a stop condition requiring investigation.

- [ ] **Step 3: Verify Pine render/alert budget and bridge exactness**

Confirm candidate `plot`, `plotshape`, `fill`, `bgcolor`, and `alertcondition` counts are not greater than 1e3. Confirm bridge constants/packing/decoder protected blocks match the baseline checks.

- [ ] **Step 4: Create release notes**

`ACW_TDI_1e4_NOTES.md` must state:
- intended behavioral change: only ACW MACD Council contribution changes mathematically;
- semantic-only changes: QUALITY and Context-TF naming/relation;
- removed dead variables;
- explicit F deferrals;
- local static verification result;
- TradingView compile/runtime still required;
- benchmark protocol: compare 1e3 vs 1e4 on BTC continuation, GOLD bearish continuation, HYPE mixed/continuation/exhaustion, and one squeeze/chop case before any threshold tuning.

- [ ] **Step 5: Package and verify ZIP integrity**

Create `/mnt/data/ACW_TDI_1e4_pair.zip` containing only `ACW_1e4.pine`, `TDI_1e4.pine`, and `ACW_TDI_1e4_NOTES.md`. Run `unzip -t` and require zero errors.

- [ ] **Step 6: Final fresh verification before reporting completion**

Re-run the full Python suite after packaging and inspect the ZIP member hashes against the standalone files. Only after this gate may 1e4 be presented as locally verified.

- [ ] **Step 7: TradingView user gate**

Load both scripts in TradingView. Required acceptance sequence: both compile; link ACW to `TDI ∞ 1e4 → TDI Bridge Bus`; confirm `QUALITY` labels have no percent sign; verify `CTX 60 ↑` on a lower-than-60m chart, `CTX 60 =` on 60m, and `CTX 60 ↓` on a higher-than-60m chart; then run the stable 1e3-vs-1e4 benchmark screenshots without threshold tuning.

---

## Self-review

- **Spec coverage:** Every included item from Sections 3–8 and verification Section 10 is assigned to Tasks 2–4. Every explicitly deferred F feature remains outside the plan.
- **Step scan:** Each implementation step changes one bounded concern; the Council change is isolated from TDI display semantics and packaging.
- **Type/name consistency:** Candidate filenames are consistently `ACW_1e4.pine` / `TDI_1e4.pine`; the wire field remains internally named confidence and is presentation-renamed only.
- **Review Focus coverage:** Council range is pinned in Task 1/2; Context relation including neutral fallback in Task 3; bridge and E logic in Task 1/3/4; render/parser budget in Task 1/4.
- **Causal visibility:** No threshold calibration is bundled into sanitation. 1e3 remains the control, and any 1e4.x threshold adjustment requires benchmark evidence.
