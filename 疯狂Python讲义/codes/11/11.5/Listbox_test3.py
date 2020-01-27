from tkinter import *
# 导入 ttk
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 创建 Listbox 组件
        self.lb = Listbox(topF)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):
            self.lb.insert(END, str(item))
        # 创建 Scrollbar 组件，设置该组件与 self.lb 的垂直滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置 self.lb 的垂直滚动影响 scroll 滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        # 为双击事件绑定事件处理方法
        self.lb.bind('<Double-1>', self.click)

    def click(self, event):
        # 获取 Listbox 当前选中项
        messagebox.showinfo(title=None, message=str(self.lb.curselection()))


root = Tk()
root.title('Listbox 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
