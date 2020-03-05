import threading


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        # 定义代表是否已经存钱的旗标
        self._flag = False

    # 因为账户余额不允许随便修改，所以只为 self._balance 提供 getter 方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的 draw() 方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁,相当于调用 Condition 绑定的 Lock 的 acquire()
        self.cond.acquire()
        try:
            # 如果 self._flag 为假，表明账户中还没有人存钱进去，取钱方法阻塞
            if not self._flag:
                self.cond.wait()
            else:
                # 执行取钱操作
                print(threading.current_thread().name
                      + " 取钱:" + str(draw_amount))
                self._balance -= draw_amount
                print("账户余额为：" + str(self._balance))
                # 将标识账户是否已有存款的旗标设为 False
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用 finally 块来释放锁
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        # 加锁，相当于调用 Condition 绑定的 Lock 的 acquire()
        self.cond.acquire()
        try:
            # 如果 self._flag 为真，表明账户中已有人存钱进去，存钱方法阻塞
            if self._flag:  # ①
                self.cond.wait()
            else:
                # 执行存款操作
                print(threading.current_thread().name \
                      + " 存款:" + str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为：" + str(self._balance))
                # 将表示账户是否已有存款的旗标设为 True
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用 finally 块来释放锁
        finally:
            self.cond.release()
