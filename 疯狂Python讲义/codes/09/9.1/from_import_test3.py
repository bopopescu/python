# 导入sys模块内的argv，winver成员
from sys import argv, winver

# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
print(winver)
