def funA(fn):
    print('A')
    # 执行传入的fn参数
    fn()
    return 'fkit'


'''
下面的装饰效果相当于funA(funB)
funB将会被替换（装饰）成该语句的返回值
由于funA函数返回fkit，因此funB就是fkit
'''


@funA
def funB():
    print('B')


print(funB)


def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))

    return bar


'''
下面的装饰效果相当于foo(my_test)
my_test将会被替换（装饰）成该语句的返回值
由于foo()函数返回bar函数，因此funB就是bar
'''


@foo
def my_test(a):
    print("===my_test函数===", a)


# 打印my_test函数，将看到实际上是bar函数
print(my_test)
# 下面代码看上去是调用my_test()，其实是调用bar()函数
my_test(10)
my_test(6, 5)


def auth(fn):
    def auth_fn(*args):
        # 哟弄个一条语句模拟执行权限检查
        print("----模拟执行权限检查----")
        # 回调被修饰的目标函数
        fn(*args)

    return auth_fn


@auth
def test(a, b):
    print("执行test函数，参数a：%s，参数b：%s:" % (a, b))


# 调用test()函数，其实是调用修饰后返回的auth_fn函数
test(20, 15)
