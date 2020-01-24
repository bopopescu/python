import itertools as it

# 使用 count(10, 3) 生成 10、13、16、…的迭代器
for e in it.count(10, 3):
    print(e)
    # 用于跳出无限循环
    if e > 20:
        break
print('----------')
my_counter = 0
# cycle 用于对序列生成无线循环的迭代器
for e in it.cycle(['Python', 'Kotlin', 'Swift']):
    print(e)
    # 用于跳出无限循环
    my_counter += 1
    if my_counter > 7:
        break
print('----------')
# repeat 用于生成 n 个元素重复的迭代器
for e in it.repeat('Python', 3):
    print(e)
