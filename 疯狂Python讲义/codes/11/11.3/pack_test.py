# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *

# 创建窗口并设置窗口标题
root = Tk()
# 设置窗口标题
root.title('Pack 布局')
for i in range(3):
    lab = Label(root, text='第 %d 个 Label' % (i + 1), bg='#eeeeee')
    # 调用 pack 进行布局
    lab.pack()
# 启动主窗口的消息循环
root.mainloop()
