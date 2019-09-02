class Rectangle:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setsize()函数
    def setsize(self, size):
        self.width, self.height = size

    # 定义getsize()函数
    def getsize(self):
        return self.width, self.height

    # 定义delsize()函数
    def delsize(self):
        self.width, self.height = 0, 0

    # 使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


# 访问size属性的说明文档
print(Rectangle.size.__doc__)
# 通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(4, 3)
# 访问rect的size属性
print(rect.size)
# 对rect的size属性赋值
rect.size = 9, 7
# 访问rect的width、height实例变量
print(rect.width)
print(rect.height)
# 删除rect的size属性
del rect.size
# 访问rect的width、height实例变量
print(rect.width)
print(rect.height)
