# 传入计算平方的lamdba表达式作为参数
x = map(lambda x: x * x, range(8))
print([e for e in x])
# 传入计算平法的lamdba表达式作为参数
y = map(lambda x: x * x if x % 2 == 0 else 0, range(8))
print([e for e in y])
