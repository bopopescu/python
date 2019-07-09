a = 5
b = 3
st = "a大于b" if a > b else "a不大于b"
print(st)
print("a大于b") if a > b else print("a不大于b")
# 第一个返回值部分使用两条语句，用逗号隔开
st = print("crazyit"), "a大于b" if a > b else "a不大于b"
print(st)
st = print("crazyit");
x = 20 if a > b else "a不大于b"
print(st)
print(x)
c = 5
d = 5
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))
