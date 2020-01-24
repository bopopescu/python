from collections import ChainMap

# 定义三个 dict 对象
a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}
# 将三个 dict 对象链在一起，就像变成了一个大的 dict
cm = ChainMap(a, b, c)
print(cm)
# 获取 Kotlin 对应的 value
print(cm['Kotlin'])
# 获取 Python 对应的 value
print(cm['Python'])
# 获取 Go 对应的 value
print(cm['Go'])
