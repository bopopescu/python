def else_test():
    s = input('请输入除数：')
    result = 20 / int(s)
    print('20除以%s的结果是：%g' % (s, result))


def right_main():
    try:
        print('try块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        else_test()


def wrong_main():
    try:
        print('try块的代码，没有异常')
        else_test()
    except:
        print('程序出现异常')


wrong_main()
right_main()
