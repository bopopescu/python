# 在字符串模版中使用key
temp = '书名是：%(name)s，价格是：%(price)010.2f，出版社是：%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子社'}
# 使用字典为字符串模版中的key传入值
print(temp % book)
book = {'name': '疯狂Kotlin讲义', 'price': 78.9, 'publish': '电子社'}
# 使用字典为字符串模版中的key传入值
print(temp % book)
