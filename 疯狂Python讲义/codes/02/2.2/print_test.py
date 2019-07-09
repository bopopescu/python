user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名：", user_name, "年龄：", user_age)
# 同时输出多个变量和字符串，指定分隔符
print("读者名：", user_name, "年龄：", user_age, sep='|')
# 设置end参数，指定输出之后不再换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
# 打开文件以便写入
f = open("poem.txt", "w", encoding='utf-8')
print('仓喊月明珠有泪', file=f)
print('烂铁日暖玉生烟', file=f)
f.close()
