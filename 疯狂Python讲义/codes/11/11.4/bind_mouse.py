# 将 tkinter 写成 Tkinter 兼容 Python 2.x
from tkinter import *


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        lb = Label(self.main, width=40, height=3)
        lb.config(bg='lightgreen', font=('Times', 20))
        # 为鼠标移动事件绑定事件处理方法
        lb.bind('<Motion>', self.motin)
        # 为按住左键时的鼠标移动事件绑定事件处理方法
        lb.bind('<B1-Motion>', self.press_motion)
        lb.pack()
        self.show = Label(self.main, width=38, height=1)
        self.show.config(bg='white', font=('Courier New', 20))
        self.show.pack()

    def motin(self, event):
        self.show['text'] = '鼠标移动到：（%s %s）' % (event.x, event.y)
        return

    def press_motion(self, event):
        self.show['text'] = '按住鼠标的位置为：（%s %s）' % (event.x, event.y)
        return


root = Tk()
root.title('鼠标事件')
App(root)
root.mainloop()
