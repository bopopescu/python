import codecs

# 指定使用 utf-8 字符集读取文件内容
f = codecs.open("for_file.py", 'r', 'utf-8', buffering=True)
# 使用 for-in 循环遍历文件对象
for line in f:
    print(line, end='')
f.close()
# 将文件对象转换为 list 列表
print(list(open("for_file.py", 'r', True, 'utf-8')))
