import codecs

# 指定使用 utf-8 字符集读取文件内容
f = codecs.open("readline_test.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一行
    line = f.readline()
    # 如果没有读到数据，跳出循环
    if not line: break
    # 输出line
    print(line, end='')
f.close()
