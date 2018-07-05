# encoding: utf-8
# import traceback
# 如果函数报错, 对某个函数最多重试 times 次.
# 输入: times, int类型, 为函数重试次数
# 调用示例:
#    @retry_several_times(3)
#    def test(aa):
#        ......


def retry_several_times(times):
    """
    通用的重连机制装饰器
    :param times: 尝试重连的次数
    :return:
    """
    if not isinstance(times, int):
        raise Exception('invalid input! input an int parameter.')

    def real_decorator(func):
        def wrapped(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i < times - 1:
                        print(u'尝试func < {0} > 第{1}次失败'.format(func.__name__, i + 1))
                        continue
                    else:
                        raise e
        return wrapped
    return real_decorator
