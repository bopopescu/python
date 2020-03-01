# 指定使用二进制方式读取文件内容
f = open("read_test3.py", 'rb', True)
# 直接读取全部文件，并调用 bytes 的 decode 将字节内容恢复成字符串
print(f.read().decode('utf-8'))
f.close()