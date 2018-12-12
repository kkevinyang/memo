# coding=utf8
import time
from functools import wraps


# 推荐 -----------------------------------
def cost_time(func):
    """
    测量函数运行速度，并打印所在模块
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.clock()
        res = func(*args, **kwargs)
        end = time.clock()

        print('function < {0} > cost_time :{1}s'.format(func.__name__, end - start))
        return res
    return wrapper
# -----------------------------------------

def cost_time():
    """
    测量函数运行速度，并打印所在模块
    """
    def deco(func):
        def _deco(*args, **kwargs):
            start = time.clock()
            res = func(*args, **kwargs)
            end = time.clock()

            print('function < {0} > cost_time :{1}s'.format(func.__name__, end - start))

            return res
        return _deco
    return deco
    

# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit4(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start_time = time.clock()
        func()
        end_time = time.clock()
        print 'used:', end_time - start_time

    # 将包装后的函数返回
    return wrapper

'''
-----------------------------------------------
使用functools.wraps(func)装饰器实现功能
'''


def timeit_3_for_wraps(func):
    @wraps(func)
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print 'used:',end-start
    return wrapper


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@timeit_3_for_wraps
def try2():
    a = 0
    for i in range(100):
        a += i



if __name__ == '__main__':
    try2()