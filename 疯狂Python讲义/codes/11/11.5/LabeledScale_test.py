from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        self.scale = ttk.LabeledScale(self.main,
                                      from_=-100,  # 设置最大值
                                      to=100,  # 设置最小值
                                      # compound=BOTTOM  # 设置显示数字的标签在下方
                                      )
        self.scale.value = -20
        self.scale.pack(fill=X, expand=YES)


root = Tk()
root.title('LabeledScale 测试')
App(root)
root.mainloop()
