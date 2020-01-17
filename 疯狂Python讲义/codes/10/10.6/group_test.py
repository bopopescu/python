import re

# 在正则表达式中使用组
m = re.search(r'(fkit).(org)', r"www.fkit.org is a good domain")
print(m.group(0))
# 调用的简化写法，底层是调用m.__getitem__(0)
print(m[0])
print(m.span(0))
print(m.group(1))
# 调用的简化写法，底层是调用m.__getitem__(1)
print(m[1])
print(m.span(1))
print(m.group(2))
# 调用的简化写法，底层是调用m.__getitem__(2)
print(m[2])
print(m.span(2))
# 返回所有组匹配的字符串组成的元组
print(m.groups())
