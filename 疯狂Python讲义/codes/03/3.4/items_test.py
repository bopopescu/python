cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取字典中所有的key-value对，返回一个dict_items对象
ims = cars.items()
print(type(ims))
# 将dict_items转换成列表
print(list(ims))
# 访问第2个key-value对
print(list(ims)[1])
# 获取字典中所有的key，返回一个dict_keys对象
kys = cars.keys()
print(type(kys))
# 将dict_keys转换成列表
print(list(kys))
# 访问第2个key
print(list(kys)[1])
# 获取字典中所有的value，返回一个dict_values对象
vals = cars.values()
print(type(vals))
# 将dict_values转换成列表
print(list(vals))
# 访问第2个key
print(list(vals)[1])
