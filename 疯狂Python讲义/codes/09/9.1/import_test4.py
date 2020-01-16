# 导入sys、os两个模块
import sys as s, os as o

# 使用模块名作为前缀来访问模块中的成员
print(s.argv[0])
# os模块的sep变量代表平台上的路径分隔符
print(o.sep)
