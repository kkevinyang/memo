# -*- coding:utf-8 -*-
import requests
from functools import wraps
import json
from django.http.response import HttpResponse


def request_method(method, **kwargs):
    """
    功能: 过滤web请求
    """

    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if method == request.method:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse(json.dumps({'code': 0, 'msg': '本接口只接受%s请求' % method}),
                                    content_type="application/json")
        return wrapper
    return decorator


@request_method('POST')
def get_ip(request):
    """
    获取IP地址的函数
    """
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    print ip


def send_http():
    """
    发出HTTP请求
    """
    url = 'www.baidu.com'
    response = requests.get(url)
    print response.content


