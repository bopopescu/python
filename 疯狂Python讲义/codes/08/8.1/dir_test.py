class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info():
        pass


# 创建一个Item对象，将之赋值给im变量
im = Item('鼠标', 29.8)
# 返回所有属性（包括方法）组成的列表
print(im.__dir__())
# 返回所有属性（包括方法）排序之后的列表
print(dir(im))
