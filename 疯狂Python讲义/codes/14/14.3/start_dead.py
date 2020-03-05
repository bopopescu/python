import threading


# 定义 action 函数准备作为线程执行体使用
def action(max):
    for i in range(100):
        print(threading.current_thread().name + " " + str(i))


# 创建线程对象
sd = threading.Thread(target=action, args=(100,))
for i in range(300):
    # 调用 threading.current_thread() 函数获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 启动线程
        sd.start()
        # 判断启动后线程的 is_alive() 值，输出 True
        print(sd.is_alive())
    # 当线程处于新建、死亡两种状态时，is_alive() 方法返回 False
    # 当 i > 20 时，该线程肯定已经启动过了，如果 sd.is_alive() 为 False 时
    # 那就是死亡状态了
    if i > 20 and not (sd.is_alive()):
        # 试图再次启动该线程
        sd.start()
