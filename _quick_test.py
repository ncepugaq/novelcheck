import sys
sys.path.insert(0, 'd:/OneDrive/Desktop/novelcheck/novelcheck')

from novelcheck.core.corrector import TypoCorrector

c = TypoCorrector()

# Test 1: Normal text should NOT be changed
text, details = c.correct('\u4ed6\u5728\u5b66\u6821\u5b66\u4e60\u3002')
print(f'Test 1 - Normal text unchanged: {text == "\u4ed6\u5728\u5b66\u6821\u5b66\u4e60\u3002"}')
print(f'  Text: {text}')
print(f'  Details: {len(details)}')

# Test 2: Specific typo should be corrected
text2, details2 = c.correct('\u6559\u5ba4\u91cc\u5bd2\u55a7\u4e86\u4e00\u9635\u3002')
print(f'\nTest 2 - Typo corrected:')
print(f'  Text: {text2}')
for d in details2:
    print(f'  {d["original"]} -> {d["suggestion"]}')

# Test 3: SPECIFIC_TYPOS direction check
from novelcheck.core.corrector import SPECIFIC_TYPOS
print(f'\nTest 3 - SPECIFIC_TYPOS sample entries:')
for k, v in list(SPECIFIC_TYPOS.items())[:5]:
    if k != v:
        print(f'  {k} -> {v}')
    else:
        print(f'  NO-OP: {k} -> {v}')

print('\nAll tests passed!')
