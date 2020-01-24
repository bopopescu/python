# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *

# 创建 Tk 对象，Tk 代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
# 创建 Label 对象，第一个参数指定将该 Label 放入 root 内
w = Label(root, text='Hello Tkinter!')
# 调用 pack 进行布局
w.pack()
# 启动主窗口
root.mainloop()
