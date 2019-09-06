def test():
    try:
        # 因为finally块中包含了return语句
        # 所以下面的return语句失去作用
        return True
    finally:
        return False


a = test()
print(a)
