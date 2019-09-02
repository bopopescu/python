def fn(self):
    print('fn函数')


# 使用type()定义Dog类
Dog = type('Dog', (object,), dict(walk=fn, age=6))
# 创建Dog对象
d = Dog()
# 分别查看d、Dog的类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
