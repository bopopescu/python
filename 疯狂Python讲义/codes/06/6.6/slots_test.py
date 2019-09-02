from builtins import print


class Dog:
    __slots__ = {'walk', 'age', 'name'}

    def __init__(self, name):
        self.name = name

    def test(self):
        print('预定义的test方法')


d = Dog('Snoopy')
from types import MethodType

# 只允许为实例动态添加walk、age、name这三个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk()
# d.foo = 30
# __slots__属性并不限制通过类来动态添加方法
Dog.bar = lambda self: print('abc')
d.bar()


class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    pass


gd = GunDog('Puppy')
# 完全可以为GunDog实例动态添加属性
gd.speed = 99
print(gd.speed)
