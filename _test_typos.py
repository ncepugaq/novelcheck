# -*- coding: utf-8 -*-
from novelcheck.core.corrector import TypoCorrector

t = TypoCorrector()

tests = [
    ("test1", "\u79bb\u5f00\u8fd9\u5ea7\u57ce\u662f"),
    ("test2", "\u5df2\u7ecf\u4e0d\u611f\u56de\u5934\u4e86"),
    ("test3", "\u613f\u524d\u8def\u5b89\u7965"),
    ("test4", "\u627e\u4e86\u5bb6\u6700\u4fbf\u610f\u7684\u65c5\u5e97"),
    ("test5", "\u68b3\u6d17\u4e86\u4e00\u7ffb"),
]

for label, text in tests:
    result, details = t.correct(text)
    status = "OK" if result != text else "FAIL"
    print(f"[{status}] {label}: {repr(text)} -> {repr(result)}")
    for d in details:
        print(f"  {d['original']} -> {d['suggestion']}")
