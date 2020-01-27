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
        # 创建 Listbox 组件
        self.lb = Listbox(topF)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            self.lb.insert(END, item)
        # 直接插入多个选项
        self.lb.insert(ANCHOR, 'Python', 'Kotlin', 'Swift', 'Ruby')
        # 创建 Scrollbar 组件，设置该组件与 self.lb 的垂直滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置 self.lb 的垂直滚动影响 scroll 滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Label(f, text='选择模式：').pack(side=LEFT)
        modes = ('multiple', 'browse', 'single', 'extended')
        self.strVar = StringVar()
        for m in modes:
            rb = ttk.Radiobutton(f, text=m, value=m,
                                 variable=self.strVar, command=self.choose_mode)
            rb.pack(side=LEFT)

    def choose_mode(self):
        print(self.strVar.get())
        self.lb['selectmode'] = self.strVar.get()


root = Tk()
root.title('Listbox 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
