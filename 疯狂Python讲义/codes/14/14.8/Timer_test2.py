from threading import Timer
import time

# 定义总共输出几次的计数器
count = 0


def print_time():
    print("当前时间：%s" % time.ctime())
    global t, count
    count += 1
    # 如果 count 小于 10，开始下一次调度
    if count < 10:
        t = Timer(1, print_time)
        t.start()


# 指定 1 秒后执行 print_time 函数
t = Timer(1, print_time)
t.start()
