import sys
import re

# 定义匹配 E-mail 的正则表达式
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+' \
              + '[\.][a-z]{2,3}([\.][a-z]{2})?'
# 读取标准输入
text = sys.stdin.read()
# 使用正则表达式执行查找
it = re.finditer(mailPattern, text, re.I)
# 输出所有的电子邮件
for e in it:
    print(str(e.span()) + "-->" + e.group())
