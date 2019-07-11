def test():
    # 外层训话
    for i in range(10):
        for j in range(10):
            print("i的值是：%d，j的值是：%d" % (i, j))
            if j == i:
                return
            print("return后的输出语句")


test()
