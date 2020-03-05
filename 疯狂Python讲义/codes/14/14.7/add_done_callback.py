from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含 2 条线程的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个 task, 50 会作为 action() 函数的参数
    future1 = pool.submit(action, 50)
    # 向线程池再提交一个 task, 100 会作为 action() 函数的参数
    future2 = pool.submit(action, 100)


    def get_result(future):
        print(future.result())


    # 为 future1 添加线程完成的回调函数
    future1.add_done_callback(get_result)
    # 为 future2 添加线程完成的回调函数
    future2.add_done_callback(get_result)
    print('--------------')
