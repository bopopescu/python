def square_gen(val):
    i = 0
    out_val = None
    while True:
        # 使用yield语句生成值，使用out_val接受send()方法发送的参数值
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        # 如果程序使用send()方法获取下一个值，out_val会获取send()方法的返回值
        if out_val is not None: print("====%d" % out_val)
        i += 1


sg = square_gen(5)
# 第一此调用send()方法获取值，只能传入None作为参数
print(sg.send(None))
print(next(sg))
print('----------')
# 调用send()方法获取生成器的下一个值，参数9会被发送给生成器
print(sg.send(9))
# 再次调用next()函数获取生成器的下一个值
print(next(sg))
# 让生成器引发异常
# sg.throw(ValueError)
# 关闭生成器
sg.close()
print(next(sg))
