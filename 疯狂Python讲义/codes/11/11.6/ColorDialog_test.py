from tkinter import *
# 导入 ttk
from tkinter import ttk
# 导入colorchooser
from tkinter import colorchooser


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建一个按钮，并为之绑定事件处理方法
        ttk.Button(self.main, text='选择颜色',
                   command=self.choose_color  # 绑定 choose_color 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def choose_color(self):
        # 调用 askcolor 函数获取所选中的颜色
        print(colorchooser.askcolor(parent=self.main, title='选择画笔颜色',
                                    color='blue'))  # 初始颜色


root = Tk()
root.title('颜色对话框测试')
App(root)
root.mainloop()
