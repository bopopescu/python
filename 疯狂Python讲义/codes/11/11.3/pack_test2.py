# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向 fm1 中添加三个按钮
        # 设置按钮从顶部开始排列，且按钮只能在水平（X）方向上填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着 fm1
        fm2.pack(side=LEFT, padx=10, expand=YES)
        # 向 fm2 中添加三个按钮
        # 设置按钮从右开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着 fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向 fm3 中添加三个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向上填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)


root = Tk()
root.title('Pack 布局')
display = App(root)
root.mainloop()
