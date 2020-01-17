import re

# 对模式中的特殊字符进行转义
print(re.escape(r'www.crazyit.org is good, i love it!'))
print(re.escape(r'A-Zand0-9?'))
