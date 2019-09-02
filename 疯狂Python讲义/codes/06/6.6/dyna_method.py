class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)


d1 = Cat('Garfield')
d2 = Cat('Kitty')
# d1.walk()
# 为Cat动态添加walk()方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func
# d1、d2调用walk()方法
d1.walk()
d2.walk()
