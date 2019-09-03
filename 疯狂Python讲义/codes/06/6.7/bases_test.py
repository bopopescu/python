class A:
    pass


class B:
    pass


class C(A, B):
    pass


print('类A的所有父类：', A.__base__)
print('类B的所有父类：', B.__base__)
print('类C的所有父类：', C.__base__)
print('类A的所有子类：', A.__subclasses__())
print('类B的所有子类：', B.__subclasses__())
