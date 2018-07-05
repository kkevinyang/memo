# -*- coding:utf-8 -*-

import time
import datetime


# 生成当前时间和天数

'''
生成当前时间戳
'''
now = time.time()

'''
生成当天日期
struct_time >> '2016-12-22 10:49:57'
'''
daytime = time.strftime('%Y-%m-%d %H:%M:%S')
datetime = time.strftime('%Y-%m-%d')  
'''
time模块生成时间标准格式
 >> struct_time
'''
localtime = time.localtime()

"""
datetime模块生成今天当前时间
 >> struct_time
"""
now_struct = datetime.datetime.now()

# time的struct_time格式 和 datetime的datetime格式 的使用

t = '2016.11.20'
ti = time.strptime(t, "%Y.%m.%d")
td = datetime.datetime.strptime(t, "%Y.%m.%d")
"""

In [70]: ti
Out[70]: time.struct_time(tm_year=2016, tm_mon=11, tm_mday=20, tm_hour=0,
        tm_min=0, tm_sec=0, tm_wday=6, tm_yday=325, tm_isdst=-1)

In [69]: td
Out[69]: datetime.datetime(2016, 11, 20, 0, 0)

In [27]: ti[0:3]
Out[27]: (2016, 11, 20)

In [31]: ti.tm_mon
Out[31]: 11

In [33]: ti.tm_mday
Out[33]: 20
"""


# 时间格式转换

"""
从时间戳到日期
1505887929.861 >> struct_time
"""
date = datetime.date.fromtimestamp(now)

"""
字符串转换成时间标准格式
'2016-12-22 10:49:57' >> struct_time
"""
strptime = time.strptime(daytime, '%Y-%m-%d %H:%M:%S')

"""
时间标准格式到时间戳
struct_time >> 1505887929.861
"""
floattime = time.mktime(localtime)



