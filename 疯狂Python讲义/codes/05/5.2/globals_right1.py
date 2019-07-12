name = 'Charlie'


def test():
    # 通过globals()函数访问name全局变量
    print(globals()['name'])
    name = '孙悟空'


test()
print(name)
