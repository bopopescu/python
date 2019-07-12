def foo():
    # 局部变量name
    name = 'Charlie'

    def bar():
        nonlocal name
        # 访问bar()函数所在foo()函数内的name局部变量
        print(name)
        name = '孙悟空'

    bar()


foo()
