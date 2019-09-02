class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是：', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        '我是一个顾客，我的爱好是：%s，地址是%s' % (self.favorite, self.address)


# Manager继承了Employee、Customer
class Manager(Employee, Customer):
    pass


m = Manager()
m.work()
m.info()
