# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, 1, 2, 2],
                   'B': [1, 2, 3, 4],
                   'C': np.random.randn(4)})
"""
>>> df
   A  B         C
0  1  1  0.362838
1  1  2  0.227877
2  2  3  1.267767
3  2  4 -0.562860
"""
print df.groupby('A').agg('min')

"""
会对每一列进行计算
   B         C
A
1  1  0.227877
2  3 -0.562860
"""
print df.groupby('A').B.agg(['min', 'max'])
"""
只选择某一列进行计算
   min  max
A          
1    1    2
2    3    4
"""

