from functools import *

# 设初始值（默认为 0）为 x，当前序列元素为 y，将 x+y 的和作为下一次计算的初始值
print(reduce(lambda x, y: x + y, range(5)))
print(reduce(lambda x, y: x + y, range(6)))
# 设初始值为 10
print(reduce(lambda x, y: x + y, range(6), 10))
print('--------------------')


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User[name=%s' % self.name


# 定义一个老式的大小比较函数，User 的 name 越长，该 User 越大
def old_cmp(u1, u2):
    return len(u1.name) - len(u2.name)


my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
# 对 my_data 排序，需要关键字函数（调用 cmp_to_key 将 old_cmp 转换为关键字函数）
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('--------------------')


@lru_cache(maxsize=32)
def factorial(n):
    print('~~计算 %d 的阶乘~~' % n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 只有这行会计算，然后会缓存 5、4、3、2、1 的阶乘
print(factorial(5))
print(factorial(3))
print(factorial(5))
print('--------------------')
# int 函数默认将十进制形式的字符串转换为整数
print(int('12345'))
# 为 int 函数的 base 参数指定参数值
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制形式的字符串转换成整数'
# 相当于执行 base 为 2 的 int 函数
print(basetwo('10010'))
print(int('10010', 2))
