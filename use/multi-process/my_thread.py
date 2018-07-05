#!/usr/bin/env python
# coding=utf-8

import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print 'thread {}, @number: {} start！！'.format(self.name, i)
            time.sleep(1)
            print 'thread {}, @number: {} stop！！'.format(self.name, i)


def main():
    print "Start main threading"
    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()

    print "End Main threading"


if __name__ == '__main__':
    main()