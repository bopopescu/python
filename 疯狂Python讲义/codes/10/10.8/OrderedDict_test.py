from collections import OrderedDict

# 创建 OrderedDict 对象
dx = OrderedDict(b=5, c=2, a=7)
print(dx)
d = OrderedDict()
# 向 OrderedDict 中添加 key-value 对
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
# 遍历 OrderedDict 的 key-value 对
for k, v in d.items():
    print(k, v)
# 创建普通的 dict 对象
my_data = {'Python': 20, 'Swift': 32, 'Kotlin': 43, 'Go': 25}
# 创建基于 key 排序的 OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
# 创建基于 value 排序的 OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1)
print(d2)
print(d1 == d2)
