from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个 Label 组件
        ttk.Label(self.master, text='选择您喜欢的图书：') \
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        books = ('疯狂 Kotlin 讲义', '疯狂 Python 讲义',
                 '疯狂 Swift 讲义', '疯狂 Java 讲义')
        i = 1
        # 采用循环创建多个 Radiobutton
        for book in books:
            ttk.Radiobutton(self.master,
                            text=book,
                            variable=self.intVar,  # 将 Radiobutton 绑定到 self.intVar 变量
                            command=self.change,  # 将选中事件绑定到 self.change 方法
                            value=i).pack(anchor=W)
            i += 1
        # 设置 Radiobutton 绑定的变量值为 2
        # 则选中 value 为 2 的 Radiobutton
        self.intVar.set(2)

    def change(self):
        from tkinter import messagebox
        # 通过 Radiobutton 绑定变量获取选中的单选钮
        messagebox.showinfo(title=None, message=self.intVar.get())


root = Tk()
root.title('Radiobutton 测试')
App(root)
root.mainloop()
