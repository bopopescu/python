import os


def test():
    fis = None
    try:
        fis = open('a.txt')
    except OSError as e:
        print(e.strerror)
        # return语句强制方法返回
        return
        # os._exit(1)
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print('执行finally块离的资源回收！')


test()
