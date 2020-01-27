from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 定义 StringVar 变量
        self.v = StringVar()
        # 创建 Listbox 组件，与 v 变量绑定
        self.lb = Listbox(topF, listvariable=self.v)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):
            self.lb.insert(END, str(item))
        # 创建 Scrollbar 组件，设置该组件与 self.lb 的垂直滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置 self.lb 的垂直滚动影响 scroll 滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Button(f, text='选中 10 项', command=self.select).pack(side=LEFT)
        Button(f, text='清除选中 3 项', command=self.clear_select).pack(side=LEFT)
        Button(f, text='删除 3 项', command=self.delete).pack(side=LEFT)
        Button(f, text='绑定变量', command=self.var_select).pack(side=LEFT)

    def select(self):
        # 选中指定项
        self.lb.selection_set(0, 9)

    def clear_select(self):
        # 取消选中指定项
        self.lb.selection_clear(1, 3)

    def delete(self):
        # 删除指定项
        self.lb.delete(5, 8)

    def var_select(self):
        # 修改与 Listbox 绑定的变量
        self.v.set(('12', '15'))


root = Tk()
root.title('Listbox 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
