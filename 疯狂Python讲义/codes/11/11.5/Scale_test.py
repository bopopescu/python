from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        self.scale = Scale(self.main,
                           from_=-100,  # 设置最大值
                           to=100,  # 设置最小值
                           resolution=5,  # 设置步长
                           label='示范 Scale',  # 设置标签内容
                           length=400,  # 设置轨道长度
                           width=30,  # 设置轨道的宽度
                           troughcolor='lightblue',  # 设置轨道的背景色
                           sliderlength=20,  # 设置滑块的长度
                           sliderrelief=SUNKEN,  # 设置显示当前值
                           showvalue=YES,  # 设置显示当前值
                           orient=HORIZONTAL  # 设置水平方向
                           )
        self.scale.pack()
        # 创建一个 Frame 作为容器
        f = Frame(self.main)
        f.pack(fill=X, expand=YES, padx=10)
        Label(f, text='是否显示值：').pack(side=LEFT)
        i = 0
        self.showVar = IntVar()
        self.showVar.set(1)
        # 创建两个 Radiobutton 控制 Scale 是否显示值
        for s in ('不显示', '显示'):
            Radiobutton(f, text=s, value=i, variable=self.showVar,
                        command=self.switch_show).pack(side=LEFT)
            i += 1
        # 创建一个 Frame 作为容器
        f = Frame(self.main)
        f.pack(fill=X, expand=YES, padx=10)
        Label(f, text='方向：').pack(side=LEFT)
        i = 0
        self.orientVar = IntVar()
        self.orientVar.set(0)
        # 创建两个 Radiobutton 控制 Scale 的方向
        for s in ('水平', '垂直'):
            Radiobutton(f, text=s, value=i, variable=self.orientVar,
                        command=self.switch_orient).pack(side=LEFT)
            i += 1

    def switch_show(self):
        self.scale['showvalue'] = self.showVar.get()

    def switch_orient(self):
        # 根据单选钮的选中状态设置 orient 选项的值
        self.scale['orient'] = VERTICAL if self.orientVar.get() else HORIZONTAL


root = Tk()
root.title('Scale 测试')
App(root)
root.mainloop()
