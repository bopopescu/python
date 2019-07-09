# 创建一个空的bytes
b1 = bytes()
print(b1)
# 创建一个空的bytes值
b2 = b''
print(b2)
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
# 调用bytes方法将字符串转换成bytes
b4 = bytes('我爱Python编程', encoding='utf-8')
print(b4)
# 利用字符串的encode()方法编码成bytes，默认使用UTF-8字符集
b5 = "学习Python很有趣".encode('utf-8')
print(b5)
# 将bytes对象编码成字符串，默认使用UTF-8进行编码
st = b5.decode('utf-8')
print(st)
