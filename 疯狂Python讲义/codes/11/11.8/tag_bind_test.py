from tkinter import *

root = Tk()
# 创建一个 Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
cv.pack()
# 创建一个 rectangle
cv.create_rectangle(30, 30, 220, 150,
                    width=8,
                    tags=('r1', 'r2', 'r3'))


def first(event):
    print('第一次的函数')


def second(event):
    print('第二次的函数')


# 为指定图形项的左键单击事件绑定处理函数
cv.tag_bind('r1', '<Button-1>', first)
# 为指定图形项的左键单击事件绑定处理函数
cv.tag_bind('r1', '<Button-1>', second, add=True)  # add 为 True 是添加，否则是替代
root.mainloop()
