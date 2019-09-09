class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times

    def info(self):
        print('一条简单的评论，内容是%s' % self.detail)


c = Comment('疯狂Python讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail'))
print(hasattr(c, 'view_times'))
print(hasattr(c, 'info'))
# 获取指定属性的属性值
print(getattr(c, 'detail'))
print(getattr(c, 'view_times'))
# 由于info是方法，故下面代码会提示：name 'info' is not defined
# print(getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)
# 设置不存在的属性，即为对象添加属性
setattr(c, 'test', '新增的测试属性')
print(c.test)


def bar():
    print('一个简单的bar方法')


# 将c的info方法设为bar函数
setattr(c, 'info', bar)
c.info()
# 将c的info设置为字符串'fkit'
setattr(c, 'info', 'fkit')
c.info()
