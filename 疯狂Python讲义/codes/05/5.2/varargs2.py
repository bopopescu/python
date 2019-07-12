# 定义了支持参数收集的函数
def test(*books, num):
    print(books)
    # books被当成元组处理
    for b in books:
        print(b)
    print(num)


# 调用test()函数
test('疯狂ios讲义', '疯狂Android讲义', num=20)
