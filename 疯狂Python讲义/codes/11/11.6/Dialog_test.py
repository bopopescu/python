from tkinter import *
# 导入 ttk
from tkinter import ttk
# 导入 simpledialog
from tkinter import simpledialog
# 导入 dialog
from tkinter import dialog


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.msg = '《疯狂 Java 讲义》历时十年沉淀，现已升级到第 4 版，' + \
                   '经过无数 Java 学习者的反复验证，被包括北京大学在内的大量 985、' + \
                   '211 高校的优秀教师引荐为参考资料，选作教材。'
        # 创建两个按钮，并为之绑定事件处理方法
        ttk.Button(self.master, text='打开 SimpleDialog',
                   command=self.open_simpledialog  # 绑定 open_simpledialog 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='代开 Dialog',
                   command=self.open_dialog  # 绑定 open_dialog 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def open_simpledialog(self):
        # 使用 simpledialog.SimpleDialog 创建对话框
        d = simpledialog.SimpleDialog(self.master,  # 设置该对话框所属的窗口
                                      title='SimpleDialog 测试',  # 标题
                                      text=self.msg,  # 内容
                                      buttons=['是', '否', '取消'],
                                      cancel=3,
                                      default=0  # 设置默认哪个按钮得到焦点
                                      )
        print(d.go())

    def open_dialog(self):
        # 使用 dialog.Dialog 创建对话框
        d = dialog.Dialog(self.master,
                          {'title': 'Dialog 测试',
                           'text': self.msg,
                           'bitmap': 'question',
                           'default': 0,
                           'strings': ('确定',
                                       '取消',
                                       '退出')})
        print(d.num)


root = Tk()
root.title('对话框测试')
App(root)
root.mainloop()
