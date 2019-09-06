import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print('您输入的两个数相乘的结果是：', c)
except (IndexError, ValueError, ArithmeticError):
    print('程序放生了数组越界、数字格式异常、算数异常之一')
except Exception:
    print('未知异常')
