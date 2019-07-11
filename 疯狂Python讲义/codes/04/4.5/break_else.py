# 一个简单的for循环
for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        # 执行该语句时将结束循环
        break
    else:
        print('else块：', i)
