import itertools as it

# 使用两个序列进行排列组合
for e in it.product('AB', 'CD'):
    print(''.join(e), end=', ')
print('\n----------')
# 使用一个序列，重复两次进行全排列
for e in it.product('AB', repeat=2):
    print(''.join(e), end=', ')
print('\n----------')
# 从序列中取两个元素进行排列
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=', ')
print('\n----------')
# 从序列中取两个元素进行组合，元素不允许重复
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=', ')
print('\n----------')
# 从序列中取两个元素进行组合，元素允许重复
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=', ')
print('\n----------')
