s = 'crazyit.org is very good'
# 获取s中索引2的字符
print(s[2])
# 获取s中从右边开始，索引4的字符
print(s[-4])
# 获取s中从索引3到索引5（不包含）的子串
print(s[3:5])
# 获取s中从索引3到倒数第5个字符的子串
print(s[3:-5])
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[-6:-3])
# 获取s中从索引5到结束的子串
print(s[5:])
# 获取s中从倒数第6个字符到结束的子串
print(s[-6:])
# 获取s中从开始到索引5的子串
print(s[:5])
# 获取s中从开始到倒数第6个字符的子串
print(s[:-6])
# 判断s是否包含'very'子串
print("very" in s)
print("fkit" in s)
# 输出s的长度
print(len(s))
# 输出'test'的长度
print(len('test'))
# 输出s字符串中的最大字符
print(max(s))
# 输出s字符串中的最小字符
print(min(s))
