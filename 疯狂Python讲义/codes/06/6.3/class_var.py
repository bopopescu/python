class Address:
    detail = '广州'
    post_code = '51060'

    def info(self):
        # 尝试直接访问类变量
        # 报错
        # print(detail)
        # 通过类来访问类变量
        print(Address.detail)
        print(Address.post_code)


# 通过类来访问Address类的类变量
print(Address.detail)
addr = Address()
addr.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()
