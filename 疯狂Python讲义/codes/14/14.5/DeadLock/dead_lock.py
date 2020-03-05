import threading
import time


class A:
    def __init__(self):
        self.lock = threading.RLock()

    def foo(self, b):
        try:
            self.lock.acquire()
            print("当前线程名: " + threading.current_thread().name \
                  + " 进入了 A 实例的 foo() 方法")  # ①
            time.sleep(0.2)
            print("当前线程名: " + threading.current_thread().name \
                  + " 企图调用 B 实例的 last() 方法")  # ③
            b.last()
        finally:
            self.lock.release()

    def last(self):
        try:
            self.lock.acquire()
            print("进入了 A 类的 last() 方法内部")
        finally:
            self.lock.release()


class B:
    def __init__(self):
        self.lock = threading.RLock()

    def bar(self, a):
        try:
            self.lock.acquire()
            print("当前线程名: " + threading.current_thread().name \
                  + " 进入了 B 实例的 bar() 方法")  # ②
            time.sleep(0.2)
            print("当前线程名: " + threading.current_thread().name \
                  + " 企图调用 A 实例的 last() 方法")  # ④
            a.last()
        finally:
            self.lock.release()

    def last(self):
        try:
            self.lock.acquire()
            print("进入了 B 类的 last() 方法内部")
        finally:
            self.lock.release()


a = A()
b = B()


def init():
    threading.current_thread().name = "主线程"
    # 调用 a 对象的 foo() 方法
    a.foo(b)
    print("进入了主线程之后")


def action():
    threading.current_thread().name = "副线程"
    # 调用 b 对象的 bar() 方法
    b.bar(a)
    print("进入了副线程之后")


# 以 action 为 target 启动新线程
threading.Thread(target=action).start()
# 调用 init() 函数
init()
