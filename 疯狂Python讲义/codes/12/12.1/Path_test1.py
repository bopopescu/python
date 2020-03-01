from pathlib import *

# 获取当前目录
p = Path('.')
# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上一级目录
p = Path('../')
# 获取上级目录及其所有子目录下的的 py 文件
for x in p.glob('**/*.py'):
    print(x)

# 获取 g:/publish/codes 对应的目录
p = Path('g:/publish/codes')
# 获取上级目录及其所有子目录下的的 py 文件
for x in p.glob('**/Path_test1.py'):
    print(x)
