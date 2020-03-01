import os

path = 'my_dir'
# 直接在当前目录下创建目录
os.mkdir(path, 0o755)
path = "abc/xyz/wawa"
# 递归创建目录
os.makedirs(path, 0o755)
