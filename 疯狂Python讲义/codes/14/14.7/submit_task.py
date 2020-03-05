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
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个 task, 50 会作为 action() 函数的参数
future1 = pool.submit(action, 50)
# 向线程池再提交一个 task, 100 会作为 action() 函数的参数
future2 = pool.submit(action, 100)
# 判断 future1 代表的任务是否结束
print(future1.done())
time.sleep(3)
# 判断 future2 代表的任务是否结束
print(future2.done())
# 查看 future1 代表的任务返回的结果
print(future1.result())
# 查看 future2 代表的任务返回的结果
print(future2.result())
# 关闭线程池
pool.shutdown()
