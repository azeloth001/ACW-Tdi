"""Source isolation audit, NOT compilation or a behavioral backtest."""
from pathlib import Path
import hashlib
import re
root = Path(__file__).resolve().parent
baseline = (root / 'baseline/ACW_1g2.pine').read_text()
candidate = (root / 'ACW_1g21_Turning_Pressure.pine').read_text()
sections = [
    ('Bridge decoder', '// Single-source F semantic bridge decoder.', 'float weightSum ='),
    ('Original G2 geometry/thresholds', '// G2 Market Phase geometry:', '// ╔═════════════════════════════════════════════════════════════════════════╗\n// ║  5. FUSION ENGINE'),
    ('Late guard and confirmed lifecycle', '// G final promotion layer.', '// ╔═════════════════════════════════════════════════════════════════════════╗\n// ║  7. SPECTRAL VISUAL ENGINE'),
    ('Alert registrations', 'alertcondition(gEntryLongEvent', None),
]
for name, start, end in sections:
    def section(text):
        text = text[text.index(start):]
        return text[:text.index(end)] if end else text
    assert section(baseline) == section(candidate), name
    print(name + ': byte-identical')
for token in ['request.security(', 'plot(', 'plotshape(', 'alertcondition(']:
    assert baseline.count(token) == candidate.count(token), token
    print(f'{token}: {candidate.count(token)} (unchanged)')
expected = '17c3a59a392d021178912be98924e765bd97950443fb430ba26d64e7a32598e6'
actual = hashlib.sha256((root/'baseline/TDI_1g.pine').read_bytes()).hexdigest()
assert actual == expected
print('TDI hash: matches supplied frozen hash')
stack = []
for number, line in enumerate(candidate.splitlines(), 1):
    line = re.sub(r'"(?:[^"\\]|\\.)*"', '""', line).split('//')[0]
    for char in line:
        if char in '([{':
            stack.append((char, number))
        elif char in ')]}':
            assert stack and '([{'.index(stack[-1][0]) == ')]}'.index(char), (number, char)
            stack.pop()
assert not stack
print('Delimiter sanity: PASS; TradingView compilation NOT performed')
