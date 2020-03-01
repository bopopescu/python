import linecache
import random

# 读取 random 模块的源文件的第 3 行
print(linecache.getline(random.__file__, 3))
# 读取本程序的第 3 行
print(linecache.getline('linecache_test.py', 3))
# 读取普通文件的第 2 行
print(linecache.getline('utf_text.txt', 2))
