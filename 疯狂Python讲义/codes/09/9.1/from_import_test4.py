# 导入sys模块中的argv，winver成员，并为其指定别名v，wv
from sys import argv as v, winver as wv

# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
print(wv)
