def test(val, step):
    print('-------函数开始执行-------')
    cur = 0
    # 遍历0-val
    for i in range(val):
        # cur添加i*step
        cur += i * step
        yield cur


# 执行函数，返回生成器
t = test(10, 2)
print('=========================')
print(next(t))
print(next(t))
for ele in t:
    print(ele, end=' ')
print('')
# 再次创建生成器
t = test(10, 1)
# 将生成及转换成列表
print(list(t))
# 再次创建生成器
t = test(10, 3)
# 将生成及转换成元组
print(tuple(t))