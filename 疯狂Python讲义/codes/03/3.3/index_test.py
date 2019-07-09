a_list = [2, 30, 'a', 'b', 'crazyit', 30]
# 定位元素30出现的位置
print(a_list.index(30))
# 从索引2开始，定位元素30出现的位置
print(a_list.index(30, 2))
# 从索引2到索引4之间定位元素30出现的位置，找不到该元素
print(a_list.index(30, 2, 4))
