# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *


# 定义继承 Frame 的 Application 类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用 initWidgets() 方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 创建 Label 对象，第一个参数指定该 Label 放入 root 内
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='images/serial.png')
        # 必须用一个不会被释放的变量以用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片是 bm
        w['image'] = bm
        w.pack()
        # 创建 Button 对象，第一个参数指定将该 Button 放入 root 内
        okButton = Button(self, text='确定')
        okButton['background'] = 'yellow'
        # okButton.configure(background='yellow')  # 与上面代码的作用相同
        okButton.pack()


# 创建 Application 对象
app = Application()
# Frame 有一个默认的 master 属性，该属性值是 Tk 对象（窗口）
print(type(app.master))
# 通过 master 属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口的消息循环
app.mainloop()
