# 定义了支持参数收集的函数
def test(a, *books):
    print(books)
    # books被当成元组处理
    for b in books:
        print(b)
    # 输出整数变量a的值
    print(a)


# 调用test()函数
test(5, '疯狂ios讲义', '疯狂Android讲义')
