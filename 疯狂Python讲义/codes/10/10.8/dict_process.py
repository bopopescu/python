s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
d = {}
for k, v in s:
    # setdefault() 方法用于获取指定 key 对应的 value
    # 如果该 key 不存在，则先将该 key 对应的 value 设置为默认值：[]
    d.setdefault(k, []).append(v)
print(list(d.items()))
