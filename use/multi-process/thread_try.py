#!/usr/bin/env python
# coding=utf-8
import threading


def fun1(func):
    # 启动线程2
    func.start()
    for i in range(5):
        print 'x', i
    func.join()
    fun2()


def fun2():
    for i in range(60):
        print 'y', i


tfunc2 = threading.Thread(target=fun2)
tfunc1 = threading.Thread(target=fun1, args=(tfunc2,))

# 启动线程1
tfunc1.start()
