# encoding: utf-8
import urllib2

import gevent
# 下面两行如果去掉就不能自动切换协程了
from gevent import monkey

from use.func.time_count import cost_time

monkey.patch_all()


def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url, timeout=15)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


@cost_time()
def open_sina():
    """
    快任务
    """
    url = 'https://www.sina.com/'
    resp = urllib2.urlopen(url, timeout=15)
    return resp.read()


@cost_time()
def open_yahoo():
    """
    慢任务
    """
    url = 'https://www.yahoo.com/'
    resp = urllib2.urlopen(url, timeout=15)
    return resp.read()


# gevent.joinall([
#         gevent.spawn(f, 'https://www.baidu.com/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://www.sina.com/'),
# ])


def main():
    gevent_work_list = []
    res1 = gevent.spawn(open_sina)
    res2 = gevent.spawn(open_yahoo)

    gevent_work_list.append(res1)
    gevent_work_list.append(res2)

    gevent.joinall(gevent_work_list)
    gevent_error_raise(gevent_work_list)

    res1 = res1.value
    res2 = res2.value

    print('res1:', res1)
    print('res2:', len(res2))


def gevent_error_raise(gevent_work_list):
    """
    协程内报错抛出
    """
    for one_gl in gevent_work_list:
        if one_gl.exception:
            # 截取第一段的报错
            message = one_gl.exception.message
            raise Exception(message)


if __name__ == '__main__':
    main()