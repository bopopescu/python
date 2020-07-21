from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 定义变量
        self.doubleVar = DoubleVar()
        self.scale = Scale(self.main,
                           from_=-100,  # 设置最大值
                           to=100,  # 设置最小值
                           resolution=5,  # 设置步长
                           label='示范 Sacle',  # 设置标签内容
                           length=400,  # 设置轨道的长度
                           width=30,  # 设置轨道的宽度
                           orient=HORIZONTAL,  # 设置水平方向
                           digits=10,  # 设置 10 位有效数字
                           command=self.change,  # 绑定事件处理方法
                           variable=self.doubleVar  # 绑定变量
                           )
        self.scale.pack()
        # 设置 Scale 的当前值
        self.scale.set(20)

    # 这个事件处理方法比较奇葩，它可以收到 Scale 的值
    def change(self, value):
        print(value, self.scale.get(), self.doubleVar.get())


root = Tk()
root.title('Scale 测试')
App(root)
root.mainloop()
