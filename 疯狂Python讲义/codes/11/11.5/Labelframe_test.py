from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建 Labelframe 容器
        lf = ttk.Labelframe(self.master, text='请选择图书',
                            padding=20)
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        books = ['Swift', 'Python', 'Kotlin', 'Ruby']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个 Radiobutton，并放入 Labelframe 中
        for book in books:
            Radiobutton(lf, text='疯狂' + book + '讲义',
                        value=i,
                        variable=self.intVar).pack(side=LEFT)
            i += 1


root = Tk()
root.title('Labelframe 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
