class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 定义析构函数
    def __del__(self):
        print('del删除对象')


im = Item('鼠标', 29.8)
x = im
del im
print('------------')
