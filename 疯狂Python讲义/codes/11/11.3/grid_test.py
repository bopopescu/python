# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建一个输入组件
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
        # 对该输入组件是使用 Pack 布局，放在容器顶部
        e.pack(side=TOP, pady=10)
        p = Frame(self.main)
        p.pack(side=TOP)
        # 定义字符串元组
        names = ('0', '1', '2', '3'
                 , '4', '5', '6', '7', '8', '9'
                 , '+', '-', '*', '/', '.', '=')
        # 遍历字符串元组
        for i in range(len(names)):
            # 创建 Button，将 Button 放入 p 组件中
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)


root = Tk()
root.title('Grid 布局')
App(root)
root.mainloop()
