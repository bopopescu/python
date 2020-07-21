from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建 Labelframe 容器
        self.lf = ttk.Labelframe(self.main, padding=20)
        self.lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 创建一个显示图片的 Label
        bm = PhotoImage(file='images/z.png')
        lb = Label(self.lf, image=bm)
        lb.bm = bm
        # 将 Labelframe 的标题设为显示图片的 Label
        self.lf['labelwidget'] = lb
        # 定义代表 Labelframe 的标题位置的 12 个常量
        self.books = ['e', 's', 'w', 'n', 'es', 'ws', 'en', 'wn',
                      'ne', 'nw', 'se', 'sw']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个 Radiobutton，并放入 Labelframe 中
        for book in self.books:
            Radiobutton(self.lf, text=book,
                        value=i,
                        command=self.change,
                        variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(9)

    def change(self):
        # 通过 labelanchor 选项改变 Labelframe 的标签的位置
        self.lf['labelanchor'] = self.books[self.intVar.get()]


root = Tk()
root.title('Labelframe 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
