from collections import Counter

# 创建空的 Counter 对象
c1 = Counter()
# 以可迭代对象创建 Counter 对象
c2 = Counter('hannah')
print(c2)
# 以可迭代对象创建 Counter 对象
c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)
# 以 dict 来创建 Counter 对象
c4 = Counter({'red': 4, 'blue': 2})
print(c4)
# 使用关键字参数的语法创建 Counter
c5 = Counter(Python=4, Swift=8)
print(c5)
