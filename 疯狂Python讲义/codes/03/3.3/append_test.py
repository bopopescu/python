a_list = ['crazyit', 20, -2]
# 追加元素
a_list.append('fkit')
print(a_list)
a_tuple = (3.4, 5.6)
# 追加元组，元组被当成一个元素
a_list.append(a_tuple)
print(a_list)
# 追加列表，列表呗当成一个元素
a_list.append(['a', 'b'])
print(a_list)
b_list = ['a', 30]
# 追加元组中的所有元素
b_list.extend((-2, 3.1))
print(b_list)
# 追加列表中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list)
# 追加区间中的所有元素
b_list.extend(range(97, 100))
print(b_list)
c_list = list(range(1, 6))
print(c_list)
# 在索引3出插入字符串
c_list.insert(3, 'CRAZY')
print(c_list)
# 在索引3出插入元组，元组被当成一个元素
c_list.insert(3, tuple('crazy'))
print(c_list)
