s = 'Hello\nCharlie\nGood\nMorning'
print(s)
s2 = '商品名\t\t单价\t\t数量\t\t总价'
s3 = '疯狂Java讲义\t108\t\t2\t\t216'
print(s2)
print(s3)
price = 108
print("the book's price is %s" % price)
user = "Charli"
age = 8
# 格式化字符串中有两个占位符，第三部分也应该提供两个变量
print("%s is a %s years old boy" % (user, age))
num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6e" % num)
print("num is: %6E" % num)
print("num is: %6s" % num)
num2 = 30
# 最小宽度为6，左边补0
print("num2 is: %06d" % num2)
# 最小宽度为6，左边补0，总带上符号
print("num2 is: %+06d" % num2)
# 最小宽度为0，左对齐
print("num2 is: %-6d" % num2)
my_value = 3.001415926535
# 最小宽度为8，小数点后保留3位
print("my_value is: %8.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0
print("my_value is: %08.3f" % my_value)
# 最小宽度为8，小数点后保留3位，左边补0，始终带符号
print("my_value is: %+08.3f" % my_value)
the_name = "Charlie"
# 指标刘3个字符
print("the name is: %.3s" % the_name)
# 指标刘2个字符，最小宽度为10
print("the name is: %10.2s" % the_name)
