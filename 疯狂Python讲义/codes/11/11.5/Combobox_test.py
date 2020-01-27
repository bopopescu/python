from tkinter import *
# 导入 ttk
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.strVar = StringVar()
        # 创建 Combobox 组件
        self.cb = ttk.Combobox(self.master,
                               textvariable=self.strVar,  # 绑定到 self.strVar 变量
                               postcommand=self.choose)  # 当用户单击下拉箭头时触发 self.choose 方法
        self.cb.pack(side=TOP)
        # 为 Combobox 配置多个选项
        self.cb['values'] = ['Python', 'Rubby', 'Kotlin', 'Swift']
        f = Frame(self.master)
        f.pack()
        self.isreadonly = IntVar()
        # 创建 Checkbutton，绑定到 self.isreadonly 变量
        Checkbutton(f, text='是否只读：',
                    variable=self.isreadonly,
                    command=self.change).pack(side=LEFT)
        # 创建 Button，点击该按钮时触发 setvalue 方法
        Button(f, text='绑定变量设置',
               command=self.setvalue).pack(side=LEFT)

    def choose(self):
        # 获取 Combobox 的当前值
        messagebox.showinfo(title=None, message=str(self.cb.get()))

    def change(self):
        self.cb['state'] = 'readonly' if self.isreadonly.get() else 'enable'

    def setvalue(self):
        self.strVar.set('我爱 Python')


root = Tk()
root.title('Combobox 测试')
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
