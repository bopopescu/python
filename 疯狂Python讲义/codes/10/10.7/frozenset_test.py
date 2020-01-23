s = set()
frozen_s = frozenset('Kotlin')
# 为 set 集合添加 frozenset
s.add(frozen_s)
print('s 集合的元素：', s)
sub_s = {'Python'}
# 为 set 集合添加普通 set 集合，程序报错
s.add(sub_s)
