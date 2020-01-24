from functools import wraps


def kc_decorator(f):
    # 让 wrapper 函数看上去就像 f 函数
    @wraps(f)
    def wrapper(*args, **kwds):
        print('调用被装饰函数')
        return f(*args, **kwds)

    return wrapper


@kc_decorator
def test():
    '''test 函数的说明信息'''
    print('执行 test 函数')


test()
print(test.__name__)
print(test.__doc__)
