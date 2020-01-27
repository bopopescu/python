from tkinter import *
# 导入 ttk
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个 Label 组件
        ttk.Label(self.master, text='选择您喜欢的人物：') \
            .pack(fill=BOTH, expand=YES)
        self.chars = []
        # 定义元组
        characters = ('孙悟空', '猪八戒', '唐僧', '牛魔王')
        # 采用循环创建多个 Checkbutton
        for ch in characters:
            intVar = IntVar()
            self.chars.append(intVar)
            cb = ttk.Checkbutton(self.master,
                                 text=ch,
                                 variable=intVar,  # 将 Checkbutton 绑定到 intVar 变量
                                 command=self.change)  # 将选中事件绑定到 self.change 方法
            cb.pack(anchor=W)
        # 创建一个 Label 组件
        ttk.Label(self.master, text='选择您喜欢的图书：') \
            .pack(fill=BOTH, expand=YES)
        # ----------下面时第二组 Checkbutton---------
        self.books = []
        # 定义两个元组
        books = ('疯狂 Python 讲义', '疯狂 Kotlin 讲义', '疯狂 Swift 讲义', '疯狂 Java 讲义')
        vals = ('python', 'kotlin', 'swift', 'java')
        i = 0
        # 采用循环创建多个 Checkbutton
        for book in books:
            strVar = StringVar()
            self.books.append(strVar)
            cb = ttk.Checkbutton(self.master,
                                 text=book,
                                 variable=strVar,  # 将 Checkbutton 绑定到 strVar 变量
                                 onvalue=vals[i],
                                 offvalue='无',
                                 command=self.books_change)  # 将选中事件绑定到 books_change 方法
            cb.pack(anchor=W)
            i += 1

    def change(self):
        # 将 self.chars 列表转换成元素为 str 的列表
        new_li = [str(e.get()) for e in self.chars]
        # 将 new_li 列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)

    def books_change(self):
        # 将 self.books 列表转换成元素为 str 的列表
        new_li = [e.get() for e in self.books]
        # 将 new_li 列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)


root = Tk()
root.title('Checkbutton 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
