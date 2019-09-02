class Bird:
    # Bird类的fly()方法
    def fly(self):
        print('我在天空离自由自在地飞翔...')


class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print('我只能在地上奔跑...')


# 创建Ostrich对象
os = Ostrich()
# 执行Ostrich对象的fyl()方法，将输出'我只能在地上奔跑...'
os.fly()
