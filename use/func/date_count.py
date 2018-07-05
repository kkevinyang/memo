# -*- coding:utf-8 -*-

import time
import datetime
import pdb

now_struct = datetime.datetime.now()


def add_days(date, add_days, format="%Y-%m-%d %H:%M:%S", need_str=False):
    """
    计算加上天数后的日期
    :param date: 传入指定日期，str or datetime.datetime
    :param add_days:需加上的天数，可为正为负，int
    :return:默认为datetime.datetime对象，need_str=True时为str
    """
    if isinstance(date, (str, unicode)):
        date = datetime.datetime.strptime(date, format)

    if not isinstance(date, datetime.datetime):
        raise Exception('传入的date格式不正确！要么是datetime.datetime要么是str')

    need_date = date + datetime.timedelta(days=add_days)

    if need_str:
        need_date = str(need_date)
    return need_date


def date_diff(date1, date2=None, need_delta=False, format="%Y-%m-%d %H:%M:%S"):
    """
    两个日期相隔多少天，如果只传入一个时间则默认是与当前时间对比

    例：2008-10-03和2008-10-01是相隔两天
    注：普通的datetime格式并没有days这一属性，只有day属性；
        days是timedelta格式特有的。

    :param need_delta:需要直接传出timedelta对象的话设为True

    使用：
        In [80]: delta
        Out[80]: datetime.timedelta(304, 51202, 576000)

        In [49]: delta.days
        Out[49]: 3

        In [52]: delta.total_seconds()  # 精确秒数
        Out[52]: 259200.0
    """
    if not isinstance(date1, (str, unicode)):
        raise Exception('请至少传入一个日期，字符格式的！')

    dt1 = datetime.datetime.strptime(date1, format)

    if not date2:
        dt2 = datetime.datetime.now()
    else:
        dt2 = datetime.datetime.strptime(date2, format)

    delta = dt2 - dt1

    if need_delta:
        return delta
    return abs(delta.days)


if __name__ == '__main__':
    date1 = '2016-12-22 10:49:57'
    date2 = '2016-1-22 10:49:57'

    days = add_days(date1, 2)
    print 'days:', days