from tkinter import *
# 导入 ttk
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建 Entry 组件
        self.entry = ttk.Entry(self.main,
                               width=44,
                               font=('StSong', 14),
                               foreground='green')
        self.entry.pack(fill=BOTH, expand=YES)
        # 创建 Text 组件
        self.text = Text(self.main,
                         width=44,
                         height=4,
                         font=('StSong', 14),
                         foreground='green')
        self.text.pack(fill=BOTH, expand=YES)
        # 创建 Frame 作为容器
        f = Frame(self.main)
        f.pack()
        # 创建五个按钮，将其放入 Frame 中
        ttk.Button(f, text='开始插入', command=self.insert_start).pack(side=LEFT)
        ttk.Button(f, text='编辑处插入', command=self.insert_edit).pack(side=LEFT)
        ttk.Button(f, text='结尾插入', command=self.insert_end).pack(side=LEFT)
        ttk.Button(f, text='获取 Entry', command=self.get_entry).pack(side=LEFT)
        ttk.Button(f, text='获取 Text', command=self.get_text).pack(side=LEFT)

    def insert_start(self):
        # 在 Entry 和 Text 的开始处插入内容
        self.entry.insert(0, 'Kotlin')
        self.text.insert(0.0, 'Kotlin')

    def insert_edit(self):
        # 在 Entry 和 Text 的编辑处插入内容
        self.entry.insert(INSERT, 'Python')
        self.text.insert(INSERT, 'Python')

    def insert_end(self):
        # 在 Entry 和 Text 的结尾处插入内容
        self.entry.insert(END, 'Swift')
        self.text.insert(END, 'Swift')

    def get_entry(self):
        messagebox.showinfo(title='输入内容', message=self.entry.get())

    def get_text(self):
        messagebox.showinfo(title='输入内容', message=self.text.get(0.0, END))


root = Tk()
root.title('Entry 测试')
App(root)
root.mainloop()
