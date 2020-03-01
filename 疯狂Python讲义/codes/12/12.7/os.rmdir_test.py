import os

path = 'my_dir'
# 直接删除当前目录下的子目录
os.rmdir(path)
path = "abc/xyz/wawa"
# 递归删除子目录
os.removedirs(path)
