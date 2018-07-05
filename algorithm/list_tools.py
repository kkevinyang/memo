#!/usr/bin/python
# coding=utf-8

# 两层展开：
s = [[1, 2], [2, 3], [1]]

print(list(set([y for x in s for y in x])))
# or
from itertools import chain
print list(chain(*s))
# or
t = []
[t.extend(i) for i in s]
# or
print sum(s, [])

# 多层展开
from collections import Iterable
ss = [1, 2, [3, 4, [5]], [6, 7]]
# flat = lambda t: [x for sub in t for x in flat(sub)] if isinstance(t, Iterable) else [t]
flat = lambda s: [x for sub in s for x in flat(sub)] if isinstance(s, Iterable) else [s]

print(flat(ss))
