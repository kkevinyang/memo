import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor, wait

Thread_Number = 4


# 示例
def example1(index):
    sleep_time = random.randint(5, 15)
    print("thread %s 准备睡 %d 秒" % (threading.current_thread().ident, sleep_time))
    time.sleep(sleep_time)  # 睡1s，模拟IO
    print("thread %s square %d" % (threading.current_thread().ident, index))
    return index * index  # 返回结果


def run():
    # 实例化线程池，thread_num个线程
    executor = ThreadPoolExecutor(Thread_Number)
    start = time.time()

    fs = []  # future列表
    for i in range(10):
        fs.append(executor.submit(example1, i))  # 提交任务

    for f in fs:
        print('result:', f.result())

    wait(fs)  # 等待计算结束

    end = time.time()
    s = sum([f.result() for f in fs])  # 求和
    print("total result=%s cost: %.2fs" % (s, end - start))
    executor.shutdown()  # 销毁线程池


if __name__ == '__main__':
    run()
