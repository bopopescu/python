from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建 Style
        style = ttk.Style()
        style.configure('fkit.TPanedwindow',
                        background='darkgray', selief=RAISED)
        # 创建 Panedwindow 组件，通过 style 属性设置分隔线
        pwindow = ttk.PanedWindow(self.master,
                                  orient=HORIZONTAL, style='fkit.TPanedwindow')
        pwindow.pack(fill=BOTH, expand=YES)
        left = ttk.Label(pwindow, text='左边标签', background='pink')
        # 调用 add 方法添加组件，每个组件占一个区域
        pwindow.add(left)
        # 创建第二个 Panedwindow 组件，该组件的方向是垂直的
        rightwindow = PanedWindow(pwindow, orient=VERTICAL)
        pwindow.add(rightwindow)
        top = Label(rightwindow, text='右上标签', background='lightgreen')
        rightwindow.add(top)
        bottom = Label(rightwindow, text='右上标签', background='lightblue')
        rightwindow.add(bottom)


root = Tk()
root.title('Panedwindow 测试')
App(root)
root.mainloop()
