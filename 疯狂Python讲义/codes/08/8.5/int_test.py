class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size

    # 定义getSize()函数
    def getSize(self):
        return self.width, self.height

    # 使用property定义属性
    size = property(getSize, setSize)

    # 定义__int__方法，程序可调用int()函数将该对象转换成整数
    def __int__(self):
        return int(self.width * self.height)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r = Rectangle(4, 5)
print(int(r))
