from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建一个位图
        bm = PhotoImage(file='images/serial.png')
        # 创建一个 Entry，同时指定 text 和 image
        self.label = ttk.Label(self.main, text='疯狂体\n系图书', \
                               image=bm, font=('StSong', 20, 'bold'), foreground='red')
        self.label.bm = bm
        # 设置 Label 默认的 compound 为 None
        self.label['compound'] = None
        self.label.pack()
        # 创建 Frame 容器，用于装多个 Radiobutton
        f = ttk.Frame(self.main)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', 'LEFT', 'RIGHT', 'TOP', 'BOTTOM', 'CENTER')
        # 定义一个 StringVar 变量，用作绑定 Radiobutton 的变量
        self.var = StringVar()
        self.var.set('None')
        # 使用循环创建多个 Radionbutton 组件
        for val in compounds:
            rb = Radiobutton(f,
                             text=val,
                             padx=20,
                             variable=self.var,
                             command=self.change_compound,
                             value=val).pack(side=LEFT, anchor=CENTER)

    def change_compound(self):
        self.label['compound'] = self.var.get().lower()


root = Tk()
root.title('compound 测试')
App(root)
root.mainloop()
