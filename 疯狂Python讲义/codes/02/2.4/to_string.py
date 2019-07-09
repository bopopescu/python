s1 = "这本书的价格是："
p = 99.8
# 字符串直接拼接数值，程序报错
# print(s1 + p)
# 使用str()将数值转换成字符串
print(s1 + str(p))
# 使用repr()将数值转换成字符串
print(s1 + repr(p))
st = "I will play my fife"
print(st)
print(repr(st))
