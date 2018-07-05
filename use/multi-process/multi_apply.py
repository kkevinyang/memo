#!/usr/bin/env python
# coding=utf-8
import time
import traceback
from multiprocessing.dummy import Pool as ThreadPool

import pandas as pd
import requests

from use.func.time_count import cost_time


@cost_time()
def muti_thread_apply(df_input, process):
    """
    针对dataframe.apply()函数的多线程改进版本

    :param df_input: 传入的初始的dataframe
    :param process: 对每一行进行的处理的process函数，可直接针对dict进行操作
    :return: 处理后的dataframe
    """
    def use_func((_, row_series)):
        row = row_series.to_dict()
        try:
            return process(row)
        except Exception as e:
            traceback.print_exc()
            raise Exception(e)

    pool = ThreadPool(len(df_input))
    print(u'开启{}个线程跑process...'.format(len(df_input)))
    results = pool.map(use_func, df_input.iterrows())
    pool.close()
    pool.join()

    # 最后还要导出为dataframe格式
    df_output = pd.DataFrame(results)
    return df_output


"""
以下是测试部分
"""


def only_cost_time_process():
    """
    一些耗时任务，测试使用
    """
    requests.get('http://www.sina.com')


def some_process():
    """
    一些耗时任务，测试使用
    """
    for _ in range(10):
        only_cost_time_process()


@cost_time()
def process(row):
    """
    process 是主函数，只需要在内部对单个dict进行操作，不需要考虑pandas的用法
    return：dict
    """
    userid = row['userid']
    row['userid_length'] = len(str(userid))
    some_process()  # 增加耗时
    return row


@cost_time()
def old_process(row):
    """
    process 是主函数，只需要在内部对单个dict进行操作，不需要考虑pandas的用法
    return：dict
    """
    userid = row['userid']
    result = {}
    result['userid_length'] = len(str(userid))
    some_process()  # 增加耗时
    return row.append(pd.Series(result))


if __name__ == "__main__":
    userids = [38543707, 8182594, 15876146, 16804075, 1682634, 99]
    df_input = pd.DataFrame({'userid': userids,
                             'flowid': [x for x in range(len(userids))],
                             'typeid': [11001] * len(userids),
                             'flow_count': [2] * len(userids)
                             })
    time1 = time.time()
    res = muti_thread_apply(df_input, process)
    # res = df_input.apply(old_process, axis=1, reduce=True)
    time2 = time.time()
    timetime = time2 - time1
    print '总耗时：', timetime
    print res
