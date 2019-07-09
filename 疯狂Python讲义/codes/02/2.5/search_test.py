s = 'crazyit.org is a good site'
# 判断s是否已crazyit开头
print(s.startswith('crazyit'))
# 判断s是否已site结尾
print(s.endswith('site'))
# 查找s中'org'出现的位置
print(s.find('org'))
# 查找s中'org'出现的位置
print(s.index('org'))
# 从索引9出开始查找s中'org'出现的位置
print(s.find('org', 9))
# print(s.index('org', 9)) # 引发错误
# 将字符串中的所有it替换成xxxx
print(s.replace('it', 'xxxx'))
# 将字符串中的1个it替换成xxxx
print(s.replace('it', 'xxxx', 1))
# 定义翻译映射表：97(a)->945(α),98(b)->945(β),116(t)->964(τ)
table = {97: 945, 98: 945, 116: 964}
print(s.translate(table))
table = str.maketrans('abt', 'αβτ')
print(table)
table = str.maketrans('abc', '123')
print(table)
