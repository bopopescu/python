import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    # 因为账户余额不允许随便修改，所以只为 self._balance 提供 getter 方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的 draw() 方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name \
                      + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name \
                      + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()
