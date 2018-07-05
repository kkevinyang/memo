#!/usr/bin/python
# coding=utf-8


def bubble_sort(l):
    """
    冒泡排序:
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j],l[i]
    return l
# print bubble_sort([2, 4, 6, 2, 5])


def quick_sort(l):
    """快速排序:
    """
    if len(l) <= 1:
        return l  # 必须返回列表
    a = l[0]
    # 此处必须是l[1:]和<=，不然就把重复的过滤掉了
    less = quick_sort([x for x in l[1:] if x <= a])
    more = quick_sort([y for y in l[1:] if y >= a])
    return less + [a] + more  # a用完后要加上列表
print quick_sort([2, 4, 6, 2, 5])
