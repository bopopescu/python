# 定义全局空间的foo函数
def foo():
    print('全局控件的foo方法')


# 定义全局空间的bar变量
bar = 20


class Bird:
    # 定义Bird空间的foo函数
    def foo():
        print('Bird空间的foo方法')

    # 定义Bird空间的bar变量
    bar = 200


# 调用全局空间的函数和变量
foo()
print(bar)
# 调用Bird空间的函数和变量
Bird.foo()
print(Bird.bar)
