import os

path = 'my_dir'
# 直接重命名当前目录下的子目录
os.rename(path, 'your_dir')
path = "abc/xyz/wawa"
# 递归重命名子目录
os.renames(path, 'foo/bar/haha')
