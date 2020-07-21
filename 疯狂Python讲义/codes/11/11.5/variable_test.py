from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        self.st = StringVar()
        # 创建 Label 组件，将其 textvariable 绑定到 self.st 变量
        ttk.Entry(self.main, textvariable=self.st,
                  width=24,
                  font=('StSong', 20, 'bold'),
                  foreground='red').pack(fill=BOTH, expand=YES)
        # 创建 Frame 作为容器
        f = Frame(self.main)
        f.pack()
        # 创建两个按钮，将其放入 Frame 中
        ttk.Button(f, text='改变', command=self.change).pack(side=LEFT)
        ttk.Button(f, text='获取', command=self.get).pack(side=LEFT)

    def change(self):
        books = ('疯狂 Python 讲义', '疯狂 Kotlin 讲义', '疯狂 Swift 讲义')
        import random
        # 改变 self.st 变量的值，与之绑定的 Entry 的内容随之改变
        self.st.set(books[random.randint(0, 2)])

    def get(self):
        from tkinter import messagebox
        # 获取 self.st 变量的值，实际上就是获取与之绑定的 Entry 中的内容
        # 并使用消息框显示 self.st 变量的值
        messagebox.showinfo(title='输入内容', message=self.st.get())


root = Tk()
root.title('variable 测试')
App(root)
root.mainloop()
