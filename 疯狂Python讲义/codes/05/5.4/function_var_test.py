# 定义一个计算乘方的函数
def pow(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


# 将pow函数赋值给my_fun，则my_fun可被当成pow使用
my_fun = pow
print(my_fun(3, 4))


# 定义一个计算面积的函数
def area(width, height):
    return width * height


# 将area函数赋值给my_fun，则my_fun可被当成area使用
my_fun = area
print(my_fun(3, 4))
