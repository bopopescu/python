from tkinter import *
# 导入 ttk
from tkinter import ttk
# 导入 simpledialog
from tkinter import simpledialog


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建三个按钮，并为之绑定事件处理方法
        ttk.Button(self.master, text='输入整数对话框',
                   command=self.open_integer  # 绑定 open_integer 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='输入浮点数对话框',
                   command=self.open_float  # 绑定 open_float 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='输入字符串对话框',
                   command=self.open_string  # 绑定 open_string 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def open_integer(self):
        # 调用 askinteger 函数生成一个让用户输入整数的对话框
        print(simpledialog.askinteger('猜糖果', '你猜我手上有几个糖果：',
                                      initialvalue=3, minvalue=1, maxvalue=10))

    def open_float(self):
        # 调用 askfloat 函数生成一个让用户输入浮点数的对话框
        print(simpledialog.askfloat('猜体重', '你猜我体重多少公斤：',
                                    initialvalue=27.3, minvalue=10, maxvalue=50))

    def open_string(self):
        # 调用 askstring 函数生成一个让用户输入字符串的对话框
        print(simpledialog.askstring('猜名字', '你猜我叫什么名字：',
                                     initialvalue='Charlie'))


root = Tk()
root.title('输入对话框测试')
App(root)
root.mainloop()
