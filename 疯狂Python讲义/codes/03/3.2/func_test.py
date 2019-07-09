# 元素都是数值的元组
a_tuple = (20, 10, -2, 15.2, 102, 50)
# 计算最大值
print(max(a_tuple))
# 计算最小值
print(min(a_tuple))
# 计算长度
print(len(a_tuple))
# 元素都是字符串的列表
b_list = ['crazyit', 'fkit', 'Python', 'Kotlin']
# 计算最大值（一次比较字符的ASCII码，先比较第一个字符，若相同，再比较第二个字符，依次类推）
print(max(b_list))  # 26个小写字母的ASCII码为97-122
# 计算最小值
print(min(b_list))  # 26个小写字母的ASCII码为65-90
# 计算长度
print(len(b_list))
