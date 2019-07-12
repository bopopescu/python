# 定义了支持参数收集的函数
def test(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


test(1, 2, 3, '疯狂ios讲义', '疯狂Android讲义', 语文=89, 数学=94)
test(1, 2, '疯狂ios讲义', '疯狂Android讲义', 语文=89, 数学=94)
test(1, 2, 语文=89, 数学=94)
