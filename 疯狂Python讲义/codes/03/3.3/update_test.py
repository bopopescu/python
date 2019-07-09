a_list = [2, 4, -3.4, 'crazyit', 23]
# 对第3个元素赋值
a_list[2] = 'fkit'
print(a_list)
# 对倒数第2个元素赋值
a_list[-2] = 9527
print(a_list)
b_list = list(range(1, 5))
print(b_list)
# 将第2个到第4个（不包含）元素赋值为新列表的元素
b_list[1:3] = ['a', 'b']
print(b_list)
# 将第3个到第3个（不包含）元素赋值为新列表的元素，就是插入元素
b_list[2:2] = ['x', 'y']
print(b_list)
# 将第3个到第6个（不包含）元素赋值为空列表，就是删除元素
b_list[2:5] = []
print(b_list)
# Python会自动将str分解成序列
b_list[1:3] = 'Charlie'
print(b_list)
c_list = list(range(1, 10))
# 指定step为2，被赋值的元素有4个，因此用于赋值的列表也必须有4个元素
c_list[2:9:2] = ['a', 'b', 'c', 'd']
print(c_list)
