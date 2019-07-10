# 外层循环
for i in range(0, 5):
    j = 0
    # 内层循环
    while j < 3:
        print("i的值为：%d，j的值为：%d" % (i, j))
        j += 1
