class Bird:
    def move(self, field):
        print('鸟在%s上自由地飞翔' % field)


class Dog:
    def move(self, field):
        print('狗在%s里飞快地奔跑' % field)


# x变量被赋值为Bird对象
x = Bird()
# 调用x变量的move()方法
x.move('天空')
# x变量被赋值为Dog对象
x = Dog()
# 调用x变量的move()方法
x.move('草地')
