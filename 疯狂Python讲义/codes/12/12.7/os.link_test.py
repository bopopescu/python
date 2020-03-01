import os

# 为 os.link_test.py 文件创建快捷方式
os.symlink('os.link_test.py', 'tt')
# 为 os.link_test.py 文件创建硬连接（Windows 上就是复制文件）
os.link('os.link_test.py', 'dst')
