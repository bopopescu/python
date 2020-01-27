from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        ttk.Label(self.master, text='指定 from、to、increament').pack()
        # 通过指定 from_、to、increment 选项创建 Spinbox
        sb1 = Spinbox(self.master, from_=20,
                      to=100,
                      increment=5)
        sb1.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='指定 values').pack()
        # 通过指定 values 选项创建 Spinbox
        self.sb2 = Spinbox(self.master,
                           values=('Python', 'Swift', 'Kotlin', 'Ruby'),
                           command=self.press)  # 通过 command 绑定事件处理方法
        self.sb2.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='绑定变量').pack()
        self.intVar = IntVar()
        # 通过指定 values 选项创建 Spinbox，并为之绑定变量
        sb3 = Spinbox(self.master,
                      values=list(range(20, 100, 4)),
                      textvariable=self.intVar,  # 绑定变量
                      command=self.press)
        sb3.pack(fill=X, expand=YES)
        self.intVar.set(33)  # 通过变量改变 Spinbox 的值

    def press(self):
        print(self.sb2.get())


root = Tk()
root.title('Spinbox 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
