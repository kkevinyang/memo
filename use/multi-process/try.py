#!/usr/bin/env python
# coding=utf-8

import time
import threading
import requests

urls = ["http://google.com", "http://yahoo.com", "http://www.baidu.com", "http://www.sina.com"]


class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        print 'thread {} start！！'.format(self.name)
        res = get_web_data(self.url)
        return res


def get_web_data(url):
    print url
    res = requests.get(url)
    print res
    return res


def main():
    print "Start main threading"
    # 创建三个线程
    threads = [MyThread(url) for url in urls]
    print 'hahaha, thread is read to run...'
    # 启动三个线程
    for t in threads:
        t.start()

    print "End Main threading"


if __name__ == '__main__':
    main()