cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)
# 弹出字典底层存储的最后一个key-value对
print(cars.popitem())
print(cars)
# 将弹出项的key赋值给k，value赋值给v
k, v = cars.popitem()
print(k, v)
