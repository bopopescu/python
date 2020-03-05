from threading import Timer


def hello():
    print("hello, world")


# 指定 10 秒后执行 hello 函数
t = Timer(10.0, hello)
t.start()
