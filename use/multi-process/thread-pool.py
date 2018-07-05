#!/usr/bin/env python
# coding=utf-8

import time
from multiprocessing.dummy import Pool as ThreadPool

import pandas as pd
import requests

from use.func.time_count import cost_time

pool = ThreadPool(6)


def get_web_data(url):
    print url, 'start!'
    time1 = time.time()
    res = requests.get('http://www.sina.com').text
    time2 = time.time()
    cost = time2 - time1
    # print url, 'end!'
    print url, 'cost:', cost
    return len(res)


@cost_time()
def main():
    # urls = ["http://google.com", "http://yahoo.com", "http://www.baidu.com", "http://www.sina.com"]
    urls = ["http://www.baidu.com", "http://www.sina.com", "http://blog.csdn.net", "http://www.jb51.net", "https://github.com"]
    results = pool.map(get_web_data, urls)
    # pdb.set_trace()
    print results
    # print pd.DataFrame(results)


@cost_time()
def only_cost_time_process():
    requests.get('http://www.sina.com')


def process(row):
    userid = row['userid']
    row['userid_length'] = len(str(userid))
    only_cost_time_process()
    return row


@cost_time()
def muti_thread_apply(df_input, process):
    def use_fun((_, row_series)):
        row = row_series.to_dict()
        return process(row)

    pool = ThreadPool(len(df_input))

    results = pool.map(use_fun, df_input.iterrows())

    df_output = pd.DataFrame(results)
    return df_output


if __name__ == "__main__":
    userids = [38543707, 8182594, 15876146, 16804075, 1682634, 99]
    df_input = pd.DataFrame({'userid': userids,
                             'flowid': [x for x in range(len(userids))],
                             'typeid': [11001] * len(userids),
                             'flow_count': [2] * len(userids)
                             })

    # res = main()
    res = muti_thread_apply(df_input, process)
    print(res)