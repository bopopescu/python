from tkinter import *

# 创建窗口
root = Tk()
root.title('操作标签')
# 创建并添加 Canvas
cv = Canvas(root, background='white', width=620, height=250)
cv.pack(fill=BOTH, expand=YES)
# 绘制一个矩形框
rt = cv.create_rectangle(40, 40, 300, 220,
                         outline='blue', width=2,
                         tag=('t1', 't2', 't3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的 id，也就是编号
print(rt)
# 绘制一个椭圆
oval = cv.create_oval(350, 50, 580, 200,
                      fill='yellow', width=0,
                      tag=('g1', 'g2', 'g3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的 id，也就是编号
print(oval)
# 根据指定 tag 该 tag 对应的所有图形项
print(cv.find_withtag('tag4'))
# 获取指定图形项的所有 tag
print(cv.gettags(rt))
print(cv.gettags(2))
cv.dtag(1, 't1')  # 删除 id 为 1 的图形项上名为 t1 的 tag
cv.dtag(oval, 'g1')  # 删除 id 为 oval 的图形项上名为 g1 的 tag
# 获取指定图形项的所有 tag
print(cv.gettags(rt))
print(cv.gettags(2))
# 为所有图形项添加 tag
cv.addtag_all('t5')
print(cv.gettags(1))
print(cv.gettags(oval))
# 为指定图形项添加 tag
cv.addtag_withtag('t6', 'g2')
# 获取指定图形项的所有 tag
print(cv.gettags(1))
print(cv.gettags(oval))
# 为指定图形项上面的图形项添加 tag, t2 上面的就是 oval 图形项
cv.addtag_above('t7', 't2')
print(cv.gettags(1))
print(cv.gettags(oval))
# 为指定图形项下面的图形项添加 tag, g2 下面的就是 rt 图形项
cv.addtag_below('t8', 'g2')
print(cv.gettags(1))
print(cv.gettags(oval))
# 为最接近指定点的图形项添加 tag，最接近 360、90 的图形项是 oval
cv.addtag_closest('t9', 360, 90)
print(cv.gettags(1))
print(cv.gettags(oval))
# 为位于指定区域内（几乎覆盖整个图形区）的最上面的图形项添加 tag
cv.addtag_closest('t10', 30, 30, 600, 240)
print(cv.gettags(1))
print(cv.gettags(oval))
# 为与指定区域内重合的最上面的图形项添加 tag
cv.addtag_closest('t11', 250, 30, 400, 240)
print(cv.gettags(1))
print(cv.gettags(oval))
root.mainloop()
