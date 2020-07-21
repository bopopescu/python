from tkinter import *
# 导入 ttk
from tkinter import ttk
# 导入 messagebox
from tkinter import messagebox as msgbox


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # ----------创建第一个 Labelframe，用于选择图标类型----------
        topF = Frame(self.main)
        topF.pack(fill=BOTH)
        lf1 = ttk.Labelframe(topF, text='请选择图标类型')
        lf1.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=5)
        i = 0
        self.iconVar = IntVar()
        self.icons = [None, 'error', 'info', 'question', 'warning']
        # 使用循环创建多个 Radiobutton，并放入 Labelframe 中
        for icon in self.icons:
            Radiobutton(lf1, text=icon if icon is not None else '默认',
                        value=i,
                        variable=self.iconVar).pack(side=TOP, anchor=W)
            i += 1
        self.iconVar.set(0)
        # ----------创建第二个 Labelframe，用于选择图标类型----------
        lf2 = ttk.Labelframe(topF, text='请选择按钮类型')
        lf2.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=5)
        i = 0
        self.typeVar = IntVar()
        # 定义所有按钮类型
        self.types = [None, 'abortretryignore', 'ok', 'okcancel',
                      'retrycancel', 'yesno', 'yesnocancel']
        # 使用循环创建多个 Radiobutton，并放入 Labelframe 中
        for tp in self.types:
            Radiobutton(lf2, text=tp if tp is not None else '默认',
                        value=i,
                        variable=self.typeVar).pack(side=TOP, anchor=W)
            i += 1
        self.typeVar.set(0)
        # ----------创建 Frame，用于包含多个按钮来生成不同的消息框----------
        bottomF = Frame(self.main)
        bottomF.pack(fill=BOTH)
        # 创建 8 个按钮，并为之绑定事件处理函数
        btn1 = ttk.Button(bottomF, text='showinfo',
                          command=self.showinfo_clicked)
        btn1.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn2 = ttk.Button(bottomF, text='showwarning',
                          command=self.showwarning_clicked)
        btn2.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn3 = ttk.Button(bottomF, text='showerror',
                          command=self.showerror_clicked)
        btn3.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn4 = ttk.Button(bottomF, text='askquestion',
                          command=self.askquestion_clicked)
        btn4.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn5 = ttk.Button(bottomF, text='askokcancel',
                          command=self.askokcancel_clicked)
        btn5.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn6 = ttk.Button(bottomF, text='askyesno',
                          command=self.askyesno_clicked)
        btn6.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn7 = ttk.Button(bottomF, text='askyesnocancel',
                          command=self.askyesnocancel_clicked)
        btn7.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)
        btn8 = ttk.Button(bottomF, text='askretrycancel',
                          command=self.askretrycancel_clicked)
        btn8.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
                  pady=5, padx=5)

    def showinfo_clicked(self):
        print(msgbox.showinfo('Info', 'showinfo 测试.',
                              icon=self.icons[self.iconVar.get()],
                              type=self.types[self.typeVar.get()]))

    def showwarning_clicked(self):
        print(msgbox.showwarning('Warning', 'showwarning 测试.',
                                 icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

    def showerror_clicked(self):
        print(msgbox.showerror('Error', 'showerror 测试.',
                               icon=self.icons[self.iconVar.get()],
                               type=self.types[self.typeVar.get()]))

    def askquestion_clicked(self):
        print(msgbox.askquestion('Question', 'askquestion 测试.',
                                 icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

    def askokcancel_clicked(self):
        print(msgbox.askokcancel('OKCancel', 'askokcancel 测试.',
                                 icon=self.icons[self.iconVar.get()],
                                 type=self.types[self.typeVar.get()]))

    def askyesno_clicked(self):
        print(msgbox.askyesno('YesNo', 'askyesno 测试.',
                              icon=self.icons[self.iconVar.get()],
                              type=self.types[self.typeVar.get()]))

    def askyesnocancel_clicked(self):
        print(msgbox.askyesnocancel('YesNoCancel', 'askyesnocancel 测试.',
                                    icon=self.icons[self.iconVar.get()],
                                    type=self.types[self.typeVar.get()]))

    def askretrycancel_clicked(self):
        print(msgbox.askretrycancel('RetryCancel', 'askretrycancel 测试.',
                                    icon=self.icons[self.iconVar.get()],
                                    type=self.types[self.typeVar.get()]))


root = Tk()
root.title('消息框测试')
App(root)
root.mainloop()
