# 定义一个函数
def girth(width, height):
    print("width:", width)
    print("height:", height)
    return 2 * (width + height)


# 传统调用函数的方式，根据位置传入参数值
print(girth(3.5, 4.8))
# 根据关键字参数来传入参数值
print(girth(width=3.5, height=4.8))
# 在使用关键字参数时刻交换位置
print(girth(height=4.8, width=3.5))
# 福分使用关键字参数，部分使用位置参数
print(girth(3.5, height=4.8))
