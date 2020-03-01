f = open('filept_test.py', 'rb')
# 判断文件指针的位置
print(f.tell())
# 将文件指针移动到3处
f.seek(3)
print(f.tell())
# 读取一个字节，文件指针自动后移 1 个数据
print(f.read(1))
print(f.tell())
# 将文件指针移动到 5 处
f.seek(5)
print(f.tell())
# 将文件指针向后移动 5 个数据
f.seek(5, 1)
print(f.tell())
# 将文件指针移动到倒数第 10 处
f.seek(-10, 2)
print(f.tell())
print(f.read(1))
