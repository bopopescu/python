books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
prices = [79, 69, 89]
# 使用zip()函数压缩两个列表，从而实现并行遍历
for book, price in zip(books, prices):
    print("%s的价格是：%5.2f" % (book, price))
a = range(10)
print([x for x in reversed(a)])
print(a)
b = ['a', 'fkit', 20, 3.4, 50]
print([x for x in reversed(b)])
c = 'Hello, Charlie'
print([x for x in reversed(c)])
a = [20, 30, -1.2, 3.5, 90, 3.6]
print(sorted(a))
print(a)
print(sorted(a, reverse=True))
b = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
print(sorted(b, key=len))
