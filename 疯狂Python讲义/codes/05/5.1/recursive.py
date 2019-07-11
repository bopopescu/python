def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        # 在函数体中调用它自身，就是函数递归
        return 2 * fn(n - 1) + fn(n - 2)


# 输出fn(10)的结果
print("fn(10)的结果是：", fn(10))
