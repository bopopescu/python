from collections import Counter

# 创建 Counter 对象
cnt = Counter()
# 访问并不存在的 key，将输出该 key 的次数为 0
print(cnt['Python'])
for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)
# 只访问 Counter 对象的元素
print(list(cnt.elements()))
# 将字符串（迭代器）转换成 Counter
chr_cnt = Counter('abracadabra')
# 获取出现最多的三个字母
print(chr_cnt.most_common(3))
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
# 用 Counter 对象执行减法，其实就是减少各元素出现的次数
c.subtract(d)
print(c)
e = Counter({'x': 2, 'y': 3, 'z': -4})
# 调用 del 删除 key-value 对，会真正删除该 key-value 对
del e['y']
print(e)
# 访问 'w' 对应的 value，'w' 没有出现过，因此返回0
print(e['w'])
# 删除 e['w']，删除该 key-value 对
del e['w']
# 再次访问 'w' 对应的 value，'w' 还是没出现，因此返回0
print(e['w'])
