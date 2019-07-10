s_max = input("请输入您想计算的阶乘：")
mx = int(s_max)
result = 1
# 使用for-in循环遍历范围
for num in range(1, mx + 1):
    result *= num
print(result)
for i in range(1, 5):
    i = 20
    print("i:", i)
