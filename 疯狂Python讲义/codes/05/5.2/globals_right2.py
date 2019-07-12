name = 'Charlie'


def test():
    # 声明name是全局变量，后面的赋值语句不会重新定义局部变量
    global name
    # 直接访问name全局变量
    print(name)
    name = '孙悟空'


test()
print(name)
