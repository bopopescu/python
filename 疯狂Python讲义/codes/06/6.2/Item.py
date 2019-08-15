class Item:
    # 直接在类命名空间中放置可执行代码
    print('这在定义Item类')
    for i in range(10):
        if i % 2 == 0:
            print('偶数：', i)
        else:
            print('奇数：', i)
