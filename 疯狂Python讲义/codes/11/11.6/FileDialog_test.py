from tkinter import *
# 导入 ttk
from tkinter import ttk
# 导入 filedialog
from tkinter import filedialog


class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()

    def initWidgets(self):
        # 创建 7 个按钮，并为之绑定事件处理方法
        ttk.Button(self.main, text='打开单个文件',
                   command=self.open_file  # 绑定 open_file 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='打开多个文件',
                   command=self.open_files  # 绑定 open_files 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='获取单个打开文件的文件名',
                   command=self.open_filename  # 绑定 open_filename 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='获取多个打开文件的文件名',
                   command=self.open_filenames  # 绑定 open_filenames 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='获取保存文件',
                   command=self.save_file  # 绑定 save_file 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='获取保存文件的文件名',
                   command=self.save_filename  # 绑定 save_filename 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.main, text='打开目录',
                   command=self.open_dir  # 绑定 open_dir 方法
                   ).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def open_file(self):
        # 调用 askopenfile 方法获取单个打开的文件
        print(filedialog.askopenfile(title='打开单个文件',
                                     filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                     initialdir='d:/'))  # 初始目录

    def open_files(self):
        # 调用 askopenfiles 方法获取多个打开的文件
        print(filedialog.askopenfiles(title='打开多个文件',
                                      filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                      initialdir='d:/'))  # 初始目录

    def open_filename(self):
        # 调用 askopenfilename 方法获取单个文件的文件名
        print(filedialog.askopenfilename(title='打开单个文件',
                                         filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                         initialdir='d:/'))  # 初始目录

    def open_filenames(self):
        # 调用 askopenfilenames 方法获取多个文件的文件名
        print(filedialog.askopenfilenames(title='打开多个文件',
                                          filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                          initialdir='d:/'))  # 初始目录

    def save_file(self):
        # 调用 asksaveasfile 方法保存文件
        print(filedialog.asksaveasfile(title='保存文件',
                                       filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                       initialdir='d:/'))  # 初始目录

    def save_filename(self):
        # 调用 asksaveasfilename 方法获取保存文件的文件名
        print(filedialog.asksaveasfilename(title='保存文件',
                                           filetypes=[('文本文件', '*.txt'), ('Python 源文件', '*.py')],  # 只处理的文件类型
                                           initialdir='d:/'))  # 初始目录

    def open_dir(self):
        # 调用 askdirectory 方法打开目录
        print(filedialog.askdirectory(title='打开目录',
                                      initialdir='d:/'))  # 初始目录


root = Tk()
root.title('文件对话框测试')
App(root)
root.mainloop()
