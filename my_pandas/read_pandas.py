# -*- coding: utf-8 -*-
import pandas as pd
# 读取数据
moyun = pd.read_csv('moyun  .csv', sep='|', encoding='gbk')
main_variable = pd.read_csv('main_variable.csv', sep='|', encoding='gbk')
print 'moyun:', moyun
print 'main_variable:', main_variable

# 去重
cols_to_use = moyun.columns.difference(main_variable.columns)
print 'cols_to_use:', cols_to_use
dfNew = pd.merge(main_variable, moyun[cols_to_use], left_index=True, right_index=True, how='outer')
result = pd.concat([moyun, main_variable], axis=1)

print u'有重复的：', result
print u'无重复的：', dfNew

# 写数据
dfNew.to_csv('myun_main.csv', index=False, sep='|', encoding='utf-8')