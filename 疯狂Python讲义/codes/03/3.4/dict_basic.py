scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])
# 对不存在的key赋值，就是增加key-value对
scores['数学'] = 93
scores[92] = 5.7
print(scores)
# 使用del语句删除key-value对
del scores['语文']
del scores['数学']
print(scores)
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 对存在的key-value对赋值，干煸key-value对
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars)
# 判断cars是否包含名为AUDI的key
print('AUDI' in cars)
# 判断cars是否包含名为PORSCHE的key
print('PORSCHE' in cars)
print('LAMBORGHINI' not in cars)
