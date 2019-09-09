class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 28.9)
print(im.__dict__)
# 通过__dict__访问name属性
print(im.__dict__['name'])
# 通过__dict__访问price属性
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)
print(im.price)
