# 首先导入线程池的包
import time
from concurrent.futures import ThreadPoolExecutor

# 创建线程池
executor = ThreadPoolExecutor(3)


# 测试方法
def test_function(num1, num2):
    print(num1, num2)
    return num1 + num2


def sleep_function(num1, num2):
    print(num1, num2)
    # 方法休眠十秒
    time.sleep(5)
    return num1 + num2


def test_submit():
    """
    单个执行
        executor.submit(function, 参数1, 参数2)
        第一个参数为具体的方法，后面为方法的参数
    """
    future = executor.submit(sleep_function, 1, 2)
    # future的result()方法可以获取到函数的执行结果
    print(future.result())


def test_map():
    """
    批量执行
        executor.map(function, 参数1_list, 参数2_list, 参数n_list)
        参数1_list: 代表方法第一个参数的列表
        参数2_list: 代表方法第二个参数的列表
        如：
            executor.map(test_function, [1, 2], [5, 5])
            代表，执行test_function方法，第一个线程的参数为1和5，第二个线程的参数为2和5。
            线程1：test_function(1, 5) 结果为1 + 5 = 6
        该方法返回的是一个可迭代的对象，里面直接包含了每个方法执行的结果，不需要调用result()方法。
        详情：https://docs.python.org/3/library/concurrent.futures.html
    """
    result_iterators = executor.map(test_function, [1, 2], [5, 5])

    for result in result_iterators:
        """
        返回：
        1 5
        2 5
        6
        7
        可以看出来是并发跑的，最后才打印结果
        """
        print(result)


def test_sleep():
    # 使用三个线程，占用线程池全部线程
    # 由于我们的结果是十秒后返回，所以这里也会被阻塞，十秒后才会收到结果
    result_iterators = executor.map(sleep_function, [1, 2, 3], [5, 6, 7])
    # 到这里很显然前面三个线程都在使用中，10秒后才能得到执行
    future = executor.submit(test_function, 4, 8)
    for result in result_iterators:
        print(result)

    print(future.result())


if __name__ == '__main__':
    test_submit()
    # test_map()
    # test_sleep()
