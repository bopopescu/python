from collections import OrderedDict

d = OrderedDict.fromkeys('abcde')
# 将 b 对应的 key-value 对移动到最右边（最后加入）
d.move_to_end('b')
print(d.keys())
# 将 b 对应的 key-value 对移动到最左边（最先加入）
d.move_to_end('b', last=False)
print(d.keys())
# 弹出并返回最右边（最后加入）的 key-value 对
print(d.popitem()[0])
# 弹出并返回最左边（最先加入）的 key-value 对
print(d.popitem(last=False)[0])
