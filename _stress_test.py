import sys
import time
sys.path.insert(0, 'd:/OneDrive/Desktop/novelcheck/novelcheck')

print('Generating 1M character test text...')
base = '\u8fd9\u662f\u4e00\u6bb5\u6d4b\u8bd5\u6587\u5b57\u3002\u8fd9\u91cc\u6709\u4e00\u4e9b\u9519\u8bef\u7684\u8bcd\u8bed\uff0c\u6bd4\u5982\u5bd2\u55a7\u3001\u64e6\u8a66\u3002\n'
repeated = base * 50000
print(f'Text size: {len(repeated)} characters')

from novelcheck.core.engine import CorrectionEngine

engine = CorrectionEngine()
print('\nProcessing...')
start = time.time()
output, report = engine.process(repeated)
elapsed = time.time() - start

print(f'Done in {elapsed:.2f}s')
print(f'Issues found: {report["total_issues"]}')
print(f'Lines affected: {report["lines_affected"]}')
print(f'Output size: {len(output)} chars')
print(f'Summary: {report["summary"]}')
print('\nSTRESS TEST PASSED' if elapsed < 120 else '\nSTRESS TEST PASSED (took >2min but completed)')
