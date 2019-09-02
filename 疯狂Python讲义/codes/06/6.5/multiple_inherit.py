class Item:
    def info(self):
        print('item中方法：', '这是一个商品')


class Product:
    def info(self):
        print('Product中方法：', '这是一个工业产品')


class Mouse(Item, Product):
    pass


m = Mouse()
m.info()


class Mouse(Product, Item):
    pass


m = Mouse()
m.info()
