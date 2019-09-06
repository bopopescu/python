s = input('请输入除数：')
try:
    result = 20 / int(s)
    '20除以%s的结果时：%g' % (s, result)
except ValueError:
    print('值错误，您必须输入数值')
except ArithmeticError:
    print('算数错误，您不能输入0')
else:
    print('没有出现异常')
