#!/usr/bin/python
# coding=utf-8

# 先看看原生的range效果
for i in range(5):
    print i
"""
    [out]:
            0
            1
            2
            3
            4
"""

print type(range(5))  # 发现range实际上是list格式
"""
    [out]:   <type 'list'>
"""


# 再看看xrange
def simple_xrange(num):
    """
    自己构造xrange
    """
    while (num):
        yield num
        num -= 1

# 1.生成器转化成列表会自动遍历
l = list(simple_xrange(8))
print l
"""
    [out]:  [8, 7, 6, 5, 4, 3, 2, 1]
"""

# 2.也可以一个个遍历
for i in simple_xrange(9):
    print i

print type(simple_xrange(9))  # 发现这次的格式是生成器
"""
    [out]:  <type 'generator'>
"""