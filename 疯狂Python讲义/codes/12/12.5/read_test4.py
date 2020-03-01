import codecs

# 指定使用 utf-8 字符集读取文件内容
f = codecs.open("read_test4.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读到数据，跳出循环
    if not ch: break
    # 输出ch
    print(ch, end='')
f.close()
