# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})


df4 = pd.DataFrame({'A': [1, 2, 3, 4],
                    'B': [5, 6, 7, 8],
                    'C': [9, 10, 11, 12],
                    'D': [13, 14, 15, 16]})

df5 = pd.DataFrame({'A': [1, 5, 3, 4],
                    'B': [5, 6, 7, 8],
                    'C': [9, 10, 16, 12],
                    'D': [12, 14, 15, 3]})


def change_name(df):
    # new_cloumns = map(lambda x: {x: 'ina' + x}, columns)
    new_cloumns = {}
    for one_field in list(df.columns):
        new_cloumns[one_field] = 'INA_' + one_field
    df = df.rename(columns=new_cloumns)
    print df
    return df


def get_index(df, column, value):
    i = df[df[column] == value].index.tolist()[0]
    return i

def common_fun():
    print df1.index
    print df1.columns


def index():
    """
    df1:
        A   B   C   D
    0  A0  B0  C0  D0
    1  A1  B1  C1  D1
    2  A2  B2  C2  D2
    3  A3  B3  C3  D3
    """
    print u'只选取第一行：'
    df1.sort_index()
    print df1[:1]
    print u'索引行，不包括右边界：'
    print df1[1:3]
    print u'索引行，包括右边界：'
    print df1.loc[1:3]
    print u'索引列，不能用切片：'
    print df1[:3][['A', 'C']]
    print u'找到C为C1的那一行:'
    print df1[df1['C'] == 'C1']
    print u'这样获取到的实际上是Series'
    print df1['C']
    print u'同上1'
    print df1.C
    print u'同上2'
    print df1.ix[0,'C']
    print 'axis:0'
    print df1.loc[[0]]
    print 'axis:1'
    print df1.loc[0]
    print '普通切片:'
    print df1[1: 3]
    print 'loc:'
    print df1.loc[[1, 3]]


def search():
    """
    df4:
       A  B   C   D
    0  1  5   9  13
    1  2  6  10  14
    2  3  7  11  15
    3  4  8  12  16
    """
    print u'查看A列值大于2的行：'
    print df4.loc[df4.loc[:, "A"] > 2, :]
    print u'查看第二行值大于2的列：'
    print df4.loc[:, df4.loc[1, :] > 2]
    print u'查看C列值s是11的行的D的值：'
    print df4.loc[df4['C'] == 11].loc[:, 'D']
    print u'同上：'
    print df4[df4['C'] == 11]['D']
    print u'获取满足条件的索引：'
    index = df4[df4['C'] == 13].index
    print len(index)
    index = df4[df4['C'] == 11].index[0]
    print index
    change(index=index)


def change(index=None):
    if index:
        df4.loc[index, 'A'] = 'nnnnnn'
        print u'修改后的df4为：'
        print df4
    else:
        print u'查看C列值s是11的行的D的值：'
        print df4[df4['C'] == 11]['D']
        # a['D'] = 'aaaaa'
        print df4
        print u'改变第一行的值：'
        df1.loc[0] = [1, 2, 3, 4]
        print df1
        print u'改变第一行某一列的值：'
        df1.loc[0, 'C'] = 'ffff'
        print df1
        print u'同上：'
        df1.ix[0, 'D'] = 'aaaa'
        print df1


def merge_and_concat():
    df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']})

    df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']})
    frames = [df1, df2, df3]
    result = pd.concat(frames)
    # df3.to_csv('df.csv', index=False, sep='|', encoding='utf-8')
    return result


def try_my():
    for x in df1.index:
        print x


def sort():
    """
    df5:
       A  B   C   D
    0  1  5   9  12
    1  5  6  10  14
    2  3  7  16  15
    3  4  8  12   3
    """
    print u'根据D列进行降序排序：'
    print df5.sort_values(['D'], ascending=False)


if __name__ == '__main__':
    # print df1
    # common_fun()
    # change()
    # search()
    # index()
    # print merge_and_concat()
    sort()

