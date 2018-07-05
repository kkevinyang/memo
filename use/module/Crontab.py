#!/usr/bin/env python
# coding=utf-8
import datetime
import tornado.gen
from tornado.ioloop import IOLoop
from functools import wraps


def call_later(delay=0):
    def wrap_loop(func):

        @wraps(func)
        def wrap_func(*args, **kwargs):
            return IOLoop.instance().call_later(delay, func, *args, **kwargs)
        return wrap_func
    return wrap_loop


def call_event(delta=60):
    _delta = delta * 1000
    _args = {'args': []}

    def wrap_loop(func):
        @wraps(func)
        @tornado.gen.coroutine
        def wrap_func(*args, **kwargs):
            ret = None
            if not _args['args']:
                _args['args'] = args
            try:
                ret = func(*_args['args'], **kwargs)
            except Exception as e:
                pass

            IOLoop.instance().add_timeout(datetime.timedelta(milliseconds=_delta), wrap_func)
            return ret
        return wrap_func
    return wrap_loop