# 序列封包：将10、20、30封装成元组后赋值给vals
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1, 10, 2))
# 序列解包：将a_tuple元组的各元素一次赋值给a、b、c、d、e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
a_list = ['fkit', 'crazyit']
# 序列解包：将a_list序列的各元素一次赋值给a_str、b_str变量
a_str, b_str = a_list
print(a_str, b_str)
# 将10、20、30依次赋值给x、y、z
x, y, z = 10, 20, 30
print(x, y, z)
# 相当于执行如下过程
# 先执行序列封包
xyz = 10, 20, 30
# 再执行序列解包
x, y, z = xyz
# y、z、x依次赋值给x、y、z
x, y, z = y, z, x
print(x, y, z)
# first、second保存前两个元素，rest列表包含剩下的元素
first, second, *rest = range(10)
print(first)
print(second)
print(rest)
# last保存最后一个元素，begin保存前面剩下的元素
*begin, last = range(10)
print(begin)
print(last)
# first保存第一个元素，last保存最后一个元素，middle保存中间剩下的元素
first, *middle, last = range(10)
print(first)
print(middle)
print(last)
