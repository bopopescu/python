from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建 Style
        style = ttk.Style()
        style.configure('fkit.TPanedwindow', background='darkgray', selief=RAISED)
        # 创建 Panedwindow 组件，通过 style 属性设置分隔线
        pwindow = ttk.PanedWindow(self.main,
                                  orient=VERTICAL, style='fkit.TPanedwindow')
        pwindow.pack(fill=BOTH, expand=1)
        first = ttk.Label(pwindow, text='第一个标签')
        # 调用 add 方法添加组件，每个组件占一个区域
        pwindow.add(first)
        okBn = ttk.Button(pwindow, text='第二个按钮',
                          # 调用 remove() 方法删除组件，该组件所在区域消失
                          command=lambda: pwindow.remove(okBn))
        # 调用 add 方法添加组件，每个组件占一个区域
        pwindow.add(okBn)
        entry = ttk.Entry(pwindow, width=30)
        # 调用 add 方法添加组件，每个组件占有一个区域
        pwindow.add(entry)
        # 调用 insert 方法插入组件
        pwindow.insert(1, Label(pwindow, text='插入的标签'))


root = Tk()
root.title('Panedwindow 测试')
App(root)
root.mainloop()
