print("5是否大于4：", 5 > 4)
print("3的4次方是否大于或等于90.0：", 3 ** 4 >= 90)
print("20是否大于或等于20.0：", 20 >= 20.0)
print("5和5.0是否相等：", 5 == 5.0)
print("True和False是否相等：", True == False)
print("1和True是否相等：", 1 == True)
print("0和False是否相等：", 0 == False)
print(True + False)
print(False - True)
import time

# 获取当前时间
a = time.gmtime()
b = time.gmtime()
print(a == b)  # a和b两个时间相等，输出True
print(a is b)  # a和b不是同一个对象，输出False
print(id(a))
print(id(b))
