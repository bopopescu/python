class User:
    def walk(self):
        print(self, '正在慢慢地走')


# 通过类调用实例方法
# User.walk()

u = User()
# 显式地为方法的第一个参数绑定参数值
User.walk(u)

# 显式地为方法的第一个参数绑定fkit字符串参数值
User.walk('fkit')
