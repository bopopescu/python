class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'

    def info(self):
        print('info方法中：', self.item)
        print('info方法中：', self.date)


rc = Record()
print(rc.item)
print(rc.date)
rc.info()
# 修改Record类的两个类变量
Record.item = '键盘'
Record.date = '2016-08-18'
# 调用info()方法
rc.info()
