# coding=utf8

import statsd
from functools import wraps
import time
import pdb

server_host = '127.0.0.1'

print('连接%s...' % server_host)

try:
    gran_client = statsd.StatsClient(server_host, 8125, prefix='patae')
except Exception:
    raise Exception('连接statsd失败!请检查环境配置')

print('连接statsd成功！！')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if ip:
        return ip
    else:
        return "127.0.0.1"


def request_statsd():
    def decorator(f):
        @wraps(f)
        def decorated_function(request):
            ip = get_client_ip(request)
            c = gran_client
            start = time.time()
            response = f(request)
            dt = int((time.time() - start) * 1000)
            # print('response:', response)
            c.incr("request.count,http_code={0},ip={1}".format(response.status_code, ip))
            c.timing("request.time,http_code={0},ip={1}".format(response.status_code, ip), dt)
            return response
        return decorated_function
    return decorator


