# 使用花括号构建 set 集合
c = {'白骨精'}
# 添加元素
c.add('孙悟空')
c.add(6)
print('c 集合的元素个数：', len(c))
# 删除制定元素
c.remove(6)
print('c 集合的元素个数：', len(c))
# 判断是否包含指定字符串
print('c 集合是否包含“孙悟空”字符串：', ('孙悟空' in c))
c.add('轻量级 Java EE 企业应用实战')
print('c 集合的元素：', c)
# 使用 set() 函数（构造器）来创建 set 集合
books = set()
books.add('轻量级 Java EE 企业应用实战')
books.add('疯狂 Java 讲义')
print('books 集合的元素：', books)
# 使用 issubset() 方法判断是否为子集合
print('books 集合是否为 c 的子集合？', books.issubset(c))
# issubset() 方法与 <= 运算符的效果相同
print('books 集合是否为 c 的子集合？', (books <= c))
# issubset 和 issuperset 其实就是相互倒过来判断
print('c 集合是否完全包含 books集合？', c.issuperset(books))
# issuper() 方法与 >= 运算符的效果相同
print('c 集合是否完全包含 books集合？', (c >= books))
# 用 c 集合减去 books 集合里的元素，不改变 c 集合本身
result1 = c - books
print(result1)
# difference() 方法也是对集合做减法，与用”-“执行运算的效果完全一样
result2 = c.difference(books)
print(result2)
# 用 c 集合减去 books 集合里的远溯，改变 c 集合本身
c.difference_update(books)
print('c 集合的元素：', c)
# 删除 c 集合里的所有元素
c.clear()
print('c 集合的元素：', c)
# 直接创建包含元素的集合
d = {'疯狂 Java 讲义', '疯狂 Python 讲义', '疯狂 Kotlin 讲义'}
print('d 集合的元素：', d)
# 计算两个集合的交集，不改变 d 集合本身
inter1 = d & books
print(inter1)
# intersection() 方法也是获取两个集合的交集，与用”&“执行计算的效果完全一样
inter2 = d.intersection(books)
print(inter2)
# 计算两个集合的交集，改变 d 集合本身
d.intersection_update(books)
print('d 集合的元素：', d)
# 将 range 对象包装成 set 集合
e = set(range(5))
f = set(range(3, 7))
print('e 集合的元素：', e)
print('f 集合的元素：', f)
# 对两个集合执行异或运算
xor = e ^ f
print('e 和 f 执行 xor 的结果：', xor)
# 计算两个集合的并集，不改变 e 集合本身
un = e.union(f)
print('e 和 f 执行并集的结果：', un)
# 计算两个集合的并集，改变 e 集合本身
e.update(f)
print('e 集合的元素：', e)
