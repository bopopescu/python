from pathlib import *

# 访问 drive 属性
print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files/').drive)
print(PurePosixPath('/etc').drive)

# 访问 root 属性
print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PurePosixPath('/etc').root)

# 访问 anchor 属性
print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)

# 访问 parents 属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])
print(pp.parents[1])
print(pp.parents[2])
print(pp.parents[3])
# 访问 parent 属性
print(pp.parent)

# 访问 name 属性
print(pp.name)
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问 suffixes 属性
print(pp.suffixes[0])
print(pp.suffixes[1])
print(pp.suffixes[2])
# 访问 suffix 属性
print(pp.suffix)
print(pp.stem)

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)
# 转成 UNIX 风格的路径
print(pp.as_posix())
# 将相对路径转换成 URI 引发异常
# print(pp.as_uri())
# 创建绝对路径
pp = PurePath('d:/', 'Python', 'Python3.6')
# 将绝对路径转换成 URI
print(pp.as_uri())

# 判断当前路径是否匹配指定模式
print(PurePath('a/b.py').match('*.py'))
print(PurePath('/a/b/c.py').match('b/*.py'))
print(PurePath('/a/b/c.py').match('a/*.py'))

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试 relative_to 方法
print(pp.relative_to('c:/'))
print(pp.relative_to('c:/abc'))
print(pp.relative_to('c:/abc/xyz'))

# 测试 with_name 方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py'))
p = PureWindowsPath('c:/')
# print(p.with_name('fkit.py'))

# 测试 with_suffix 方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))
