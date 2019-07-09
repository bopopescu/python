s = 'crazyit.org is a good site'
# 使用空白字符串进行分割
print(s.split())
# 使用空白字符串进行分割，最多只分割前两个单词
print(s.split(None, 2))
# 使用点进行分割
print(s.split('.'))
mylist = s.split()
# 使用'/'作为分割服，将mylist连接成字符串
print('/'.join(mylist))
# 使用','作为分割服，将mylist连接成字符串
print(','.join(mylist))
