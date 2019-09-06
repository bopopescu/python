import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print('您输入的两个数相乘的结果是：', c)
except IndexError:
    print('索引错误：运行程序时输入的参数个数不够')
except ValueError:
    print('数值错误：程序只能接受整数参数')
except ArithmeticError:
    print('算数错误')
except Exception:
    print('未知异常')
