from tkinter import *
# 导入 ttk
from tkinter import ttk
from tkinter import messagebox as msgbox


class App:
    def __init__(self, master):
        self.master = master
        self.init_menu()

    # 创建菜单
    def init_menu(self):
        # 创建 menubar，它被放入 self.master 中
        menubar = Menu(self.master)
        self.master.filenew_icon = PhotoImage(file='images/filenew.png')
        self.master.fileopen_icon = PhotoImage(file='images/fileopen.png')
        # 添加菜单条
        self.master['menu'] = menubar
        # 创建 file_menu 菜单，它被放入 menubar 中
        file_menu = Menu(menubar, tearoff=0)
        # 使用 add_cascade 方法添加 lang_menu 菜单
        menubar.add_cascade(label='文件', menu=file_menu)
        # 使用 lang_menu 菜单，它被放入 menubar 中
        lang_menu = Menu(menubar, tearoff=0)
        # 使用 add_cascade 方法添加 lang_menu 菜单
        menubar.add_cascade(label='选择语言', menu=lang_menu)
        # 使用 add_command 方法为 file_menu 添加菜单项
        file_menu.add_command(label='新建', command=None,
                              image=self.master.filenew_icon, compound=LEFT)
        file_menu.add_command(label='打开', command=None,
                              image=self.master.fileopen_icon, compound=LEFT)
        # 使用 add_separator 方法为 file_menu 添加分割条
        file_menu.add_separator()
        # 为 file_menu 创建子菜单
        sub_menu = Menu(file_menu, tearoff=0)
        # 使用 add_cascade 方法添加 sub_menu 子菜单
        file_menu.add_cascade(label='选择性别', menu=sub_menu)
        self.genderVar = IntVar()
        # 使用循环为 sub_menu 子菜单添加菜单项
        for i, im in enumerate(['男', '女', '保密']):
            # 使用 add_radiobutton 方法为 sub_menu 子菜单添加单选菜单项
            # 绑定同一个变量，说明他们是一组的
            sub_menu.add_radiobutton(label=im, command=self.choose_gender,
                                     variable=self.genderVar, value=i)
        self.langVars = [StringVar(), StringVar(), StringVar(), StringVar()]
        # 使用循环为 lang_menu 菜单添加菜单项
        for i, im in enumerate(('Python', 'Kotlin', 'Swift', 'Java')):
            # 使用 add_checkbutton 方法为 lang_menu 菜单添加多选菜单项
            lang_menu.add_checkbutton(label=im, command=self.choose_lang,
                                      onvalue=im, variable=self.langVars[i])

    def choose_gender(self):
        msgbox.showinfo(message=('选择的性别为：%s' % self.genderVar.get()))

    def choose_lang(self):
        rt_list = [e.get() for e in self.langVars]
        msgbox.showinfo(message=('选择的语言为：%s' % ','.join(rt_list)))


root = Tk()
root.title('菜单测试')
# 禁止改变窗口大小
root.resizable(width=False, height=False)
App(root)
root.mainloop()
