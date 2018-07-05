# -*- coding: utf-8 -*-
import pandas as pd
columns = [
    'a',
    'b',
    'c',
    'd',
]
# 1.
# a=['a']
# a.extend([-1] * (len(columns) - 1))
# print a

# 2.
row_seires = pd.Series([-1 for i in range(len(columns))], index=columns)
row_seires.append()
row_seires['b'] = 333
print row_seires

for x in row_seires.index:
    print '%s:%s' % (x, row_seires[x])

