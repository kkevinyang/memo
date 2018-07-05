#!/usr/bin/python
# coding=utf-8


def cal_drinks(n):
    """
    一个汽水是$1, 两个汽水的空瓶换一瓶可乐, 请问给一些钱, 最多能喝几瓶呢? 
    """
    avail_drinks = n
    sum_drunk = 0
    empty_drinks = 0
    while avail_drinks or empty_drinks:
        sum_drunk += avail_drinks / 2
        empty_drinks = avail_drinks % 2
