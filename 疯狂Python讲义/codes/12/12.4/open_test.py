# 以默认方式打开文件
f = open('open_test.py')
# 访问文件的编码方式
print(f.encoding)
# 访问文件的访问模式
print(f.mode)
# 访问文件是否已经关闭
print(f.closed)
# 访问文件对象打开的文件名
print(f.name)
