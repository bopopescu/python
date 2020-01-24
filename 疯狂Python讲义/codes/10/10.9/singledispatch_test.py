from functools import *


@singledispatch
def test(arg, verbose):
    if verbose:
        print('默认参数为：', end=' ')
    print(arg)


# 限制 test 函数的第一个参数为 int 类型的函数版本
@test.register(int)
def _(argu, verbose):
    if verbose:
        print('整形参数为：', end=' ')
    print(argu)


test('Python', True)
# 调用第一个参数为 int 类型的版本
test(20, True)


@test.register(list)
def _(argb, verbose=False):
    if verbose:
        print('列表中所有元素为：')
    for i, elem in enumerate(argb):
        print(i, elem, end=' ')


test([20, 10, 16, 30, 14], True)
print('\n--------------------')


# 定义一个函数，不适用函数装饰器修饰
def nothing(arg, verbose=False):
    print('~~None 参数~~')


# 当 test 函数的第一个参数为 None 类型时，转向调用 nothing 函数
test.register(type(None), nothing)
test(None, True)
print('\n--------------------')
from decimal import Decimal


# 限制 test 函数的第一个参数 float 或 Decimal 类型的函数版本
@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print('参数的一半为：', end=' ')
    print(arg / 2)


# 通过 test.dispatch(类型) 即可获取她转向的函数
# 当 test 函数的第一个参数为 float 时将转向调用 test_num
print(test_num is test.dispatch(float))
# 当 test 函数的第一个参数为 Decimal 时将转向调用 test_num
print(test_num is test.dispatch(Decimal))
# 直接调用 test 并不等于调用 test_num
print(test_num is test)
# 获取 test 函数所绑定的全部类型
print(test.registry.keys())
# 获取 test 函数为 int 类型绑定的函数
print(test.registry[int])
