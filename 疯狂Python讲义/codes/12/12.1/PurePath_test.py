from pathlib import *

# 创建 PurePath，实际上使用 PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))
pp = PurePath('crazyit', 'some/path', 'info')
# 看到输出 Windows 风格的路径
print(pp)
pp = PurePath(Path('crazyid'), Path('info'))
# 看到输出 Windows 风格的路径
print(pp)
# 明确指定创建 PurePosixPath
pp = PurePosixPath('crazyit', 'some/path', 'info''')
# 看到输出 UNIX 风格的路径
print(pp)
# 如果不传入参数，默认使用当前路径
pp = PurePath()
print(pp)
# 如果传入的参数包含多个根路径，则只有最后一个根路径及后面的子路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)
pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp)
# 在Windows 风格的路径中，只有盘符才算根路径
pp = PureWindowsPath('c:/Windows', '/Program Files')
print(pp)
# 在路径字符串中多出来的斜杠和点号（代表当前路径）都会被忽略
pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp)
