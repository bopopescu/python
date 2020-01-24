import itertools as it

# 默认使用累加的方式计算下一个元素的值
for e in it.accumulate(range(6)):
    print(e, end=', ')
print('\n----------')
# 使用 x*y 的方式来计算迭代器下一个元素的值
for e in it.accumulate(range(1, 6), lambda x, y: x * y):
    print(e, end=', ')
print('\n----------')
# 将两个序列“链”在一起，生成新的迭代器
for e in it.chain(['a', 'b'], ['Kotlin', 'Swift']):
    print(e, end=', ')
print('\n----------')
# 根据第二个序列来筛选第一个序列的元素
# 由于第二个序列只有中间两个元素为 1（True），因此第一个序列只保留中间两个元素
for e in it.compress(['a', 'b', 'Kotlin', 'x', 'y'], [0, 1, 1, 0]):
    print(e, end=', ')
print('\n----------')
# 获取序列中从长度不小于 4 的元素开始到结束的所有元素
for e in it.dropwhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n----------')
# 去掉序列中从长度不小于 4 的元素开始到结束的所有元素
for e in it.takewhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n----------')
# 只保留序列中长度不小于 4 的元素
for e in it.filterfalse(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n----------')
# 使用 pow 函数对原序列的元素进行计算，将计算结果作为新序列的元素
for e in it.starmap(pow, [(2, 5), (3, 2), (10, 3)]):
    print(e, end=', ')
print('\n----------')
# 将 'ABCD'、'xy' 的元素按索引合并成元组，这些元组将作为新序列的元素
# 长度不够的序列元素使用 '-' 字符代替
for e in it.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(e, end=', ')
print('\n----------')
