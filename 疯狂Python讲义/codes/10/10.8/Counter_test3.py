from collections import Counter

# 创建 Counter 对象
c = Counter(Python=4, Swift=2, Kotlin=3, Go=-2)
# 统计 Counter 中所有元素出现次数的总和
print(sum(c.values()))
# 将 Counter 转换为 list，只保留各 key
print(list(c))
# 将 Counter 转换为 set，只保留各 key
print(set(c))
# 将 Counter 转换为 dict
print(dict(c))
# 将 Counter 转换为 list，列表元素都是 (元素, 出现次数) 组
list_of_pairs = c.items()
print(list_of_pairs)
# 将列表元素为 (元素, 出现次数) 组的 list 转换为 Counter
c2 = Counter(dict(list_of_pairs))
print(c2)
# 获取 Counter 中最少出现的三个元素
print(c.most_common()[:-4:-1])
# 清空所有 key-value 对
c.clear()
print(c)
c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)
# 对 Counter 执行加法
print(c + d)
# 对 Counter 执行减法
print(c - d)
# 对 Counter 执行交运算
print(c & d)
print(c | d)
print(+c)
print(-d)
