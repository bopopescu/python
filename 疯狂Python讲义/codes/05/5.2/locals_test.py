def test():
    age = 20
    # 直接访问age局部变量
    print(age)
    # 访问函数局部范围内的“变量数组”
    print(locals())
    # 通过函数局部范围内的“变量数组”访问age变量
    print(locals()['age'])
    # 通过locals函数局部范围内的“变量数组”改变age变量的值
    locals()['age'] = 12
    # 再次访问age变量的值
    print('xxx', age)
    # 公国globals函数修改x全局变量
    globals()['x'] = 19


x = 5
y = 20
print(globals())
print(locals())
# 直接访问x全局变量
print(x)
# 通过全局变量的“变量数组”访问x全局变量
print(globals()['x'])
# 通过全局变量的“变量数组”对x全局变量赋值
globals()['x'] = 39
print(x)
