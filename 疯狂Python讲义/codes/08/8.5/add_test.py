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

    # 定义__add__方法，该对象可执行“+”运算
    def __add__(self, other):
        # 要求参与“+”运算的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('+运算的另一个操作数必须是Rectangle')
        return Rectangle(self.width + other.width, self.height + other.height)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
# 对两个Rectangle执行加法运算
r = r1 + r2
print(r)
