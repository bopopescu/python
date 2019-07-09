print(help(str.lstrip))
s = '  this is a puppy  '
# 删除左边的空白
print(s.strip())
# 删除右边的空白
print(s.rstrip())
# 删除两边的空白
print(s.strip())
# 再次输出s，将会看到s并没有改变
print(s)
s2 = 'i think it is a scarecrow'
# 删除左边的i、t、o、w字符
print(s2.lstrip('itow'))
# 删除右边的i、t、o、w字符
print(s2.rstrip('itow'))
# 删除两边的i、t、o、w字符
print(s2.strip('itow'))
