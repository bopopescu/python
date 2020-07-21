from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        self.sv = StringVar()
        # 创建一个 OptionMenu 组件
        self.om = ttk.OptionMenu(root,
                                 self.sv,  # 绑定变量
                                 'Python',  # 设置初始选中值
                                 'Kotlin',  # 以下多个值用于设置菜单项
                                 'Ruby',
                                 'Swift',
                                 'Java',
                                 'Python',
                                 'JavaScript',
                                 'Erlang',
                                 command=self.print_option)  # 绑定事件处理方法
        self.om.pack()
        # 创建 Labelframe 容器
        lf = ttk.Labelframe(self.main, padding=20, text='请选择菜单方向')
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 定义代表 Labelframe 的标签位置的 12 个常量
        self.directions = ['below', 'above', 'left', 'right', 'flush']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个 Radiobutton，并放入 Labelframe 中
        for direct in self.directions:
            Radiobutton(lf, text=direct,
                        value=i,
                        command=self.change,
                        variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(9)

    def print_option(self, val):
        # 通过两种方式来获取 OptionMenu 选中的菜单项的值
        print(self.sv.get(), val)

    def change(self):
        # 通过 direction 选项改变 OptionMenu 中菜单项的值
        self.om['direction'] = self.directions[self.intVar.get()]


root = Tk()
root.title('OptionMenu 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
