from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个 Label 组件
        ttk.Label(self.master, text='选择您喜欢的兵种：') \
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        races = ('z.png', 'p.png', 't.png')
        raceNames = ('虫族', '神族', '人族')
        i = 1
        # 采用循环创建多个 RadioButton
        for rc in races:
            bm = PhotoImage(file='images/' + rc)
            r = ttk.Radiobutton(self.master,
                                image=bm,
                                text=raceNames[i - 1],
                                compound=RIGHT,  # 图片在文字右边
                                variable=self.intVar,  # 将 Radiobutton 绑定到 self.intVar 变量
                                command=self.change,  # 将选中事件绑定到 self.change 方法
                                value=i)
            r.bm = bm
            r.pack(anchor=W)
            i += 1
        # 设置默认选中 value 为 2 的单选钮
        self.intVar.set(2)

    def change(self):
        pass


root = Tk()
root.title('Radiobutton 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
