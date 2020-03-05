import threading


# 定义准备作为线程执行体的 action 函数
def action(max):
    for i in range(max):
        # 直接调用 run() 方法时，Thread 的 name 属性返回的是该对象的名字
        # 而不是当前线程的名字
        # 使用 threading.current_thread().name 总是获取当前线程的名字
        print(threading.current_thread().name + " " + str(i))  # ①


for i in range(100):
    # 调用 Thread 的 currentThread() 方法获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 直接调用线程对象的 run() 方法
        # 系统会把线程对象当成普通对象，把 run() 方法当成普通方法
        # 所以下面两行代码并不会启动两个线程，而是依次执行两个 run() 方法
        threading.Thread(target=action, args=(100,)).run()
        threading.Thread(target=action, args=(100,)).run()
