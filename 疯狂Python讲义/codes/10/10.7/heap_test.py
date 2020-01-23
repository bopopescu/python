from heapq import *

my_data = list(range(10))
my_data.append(0.5)
# 此时 my_data 依然使一个 list 列表
print('my_data 的元素：', my_data)
# 对 my_data 应用堆属性
heapify(my_data)
print('应用堆之后 my_data 的元素：', my_data)
heappush(my_data, 7.2)
print('添加 7.2 之后 my_data 的元素：', my_data)
# 弹出堆中最小的元素
print(heappop(my_data))
print(heappop(my_data))
print('弹出两个元素之后 my_data 的元素：', my_data)
# 弹出最小的元素，压入指定元素
print(heapreplace(my_data, 8.1))
print('执行 replace 之后 my_data 的元素：', my_data)
print('my_data 中最大的 3 个元素：', nlargest(3, my_data))
print('my_data 中最小的 4 个元素：', nsmallest(4, my_data))
