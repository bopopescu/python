import re

m1 = re.match('www', 'www.fkit.org')  # 从开始位置匹配
print(m1.span())  # span返回匹配的位置
print(m1.group())  # group返回匹配的组
print(re.match('fkit', 'www.fkit.org'))  # 如果从开始位置匹配不到，返回None
m2 = re.search('www', 'www.fkit.org')  # 从开始位置匹配
print(m2.span())
print(m2.group())
m3 = re.search('fkit', 'www.fkit.com')  # 从中间位置匹配，返回Match对象
print(m3.span())
print(m3.group())
