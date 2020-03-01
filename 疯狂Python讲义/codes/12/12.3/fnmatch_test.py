from pathlib import *
import fnmatch

# 遍历当前目录下所有文件和子目录
for file in Path('.').iterdir():
    # 访问所有以 _test.py 结尾的文件
    if fnmatch.fnmatch(file, '*_test.PY'):
        print(file)

names = ['a.py', 'b.py', 'c.py', 'd.py']
# 对 names 列表进行过滤
sub = fnmatch.filter(names, '[ac].py')
print(sub)

print(fnmatch.translate('?.py'))
print(fnmatch.translate('[ac].py'))
print(fnmatch.translate('[a-c].py'))
