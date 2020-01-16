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

    # 定义__gt__方法，该对象可支持“>”和“<”比较
    def __gt__(self, other):
        # 要求参与“>”比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>比较要求目标是Rectangle')
        return True if self.width * self.height > other.width * other.height else False

    # 定义__eq__方法，该对象可支持“==”和“!=”比较
    def __eq__(self, other):
        # 要求参与“==”比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('==比较要求目标是Rectangle')
        return True if self.width * self.height == other.width * other.height else False

    # 定义__ge__方法，该对象可支持“>=”和“<=”比较
    def __ge__(self, other):
        # 要求参与“>=”比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>=比较要求目标是Rectangle')
        return True if self.width * self.height >= other.width * other.height else False

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 == r2)
print(r1 != r2)
print('--------------------')
r3 = Rectangle(2, 6)
print(r2 >= r3)
print(r2 > r3)
print(r2 <= r3)
print(r2 < r3)
print(r2 == r3)
print(r2 != r3)
