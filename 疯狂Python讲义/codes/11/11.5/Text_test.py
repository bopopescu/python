from tkinter import *
# 导入 ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个 Text 组件
        text1 = Text(self.master, height=27, width=32)
        # 创建图片
        book = PhotoImage(file='images/java.png')
        text1.bm = book
        text1.insert(END, '\n')
        # 在结尾处插入图片
        text1.image_create(END, image=book)
        text1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 创建第二个 Text 组件
        text2 = Text(self.master, height=33, width=50)
        text2.pack(side=LEFT, fill=BOTH, expand=YES)
        self.text = text2
        # 创建 Scrollbar 组件，设置该组件与 text2 的垂直滚动关联
        scroll = Scrollbar(self.master, command=text2.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置 text2 的垂直滚动影响 scroll 滚动条
        text2.configure(yscrollcommand=scroll.set)
        # 配置名为 title 的样式
        text2.tag_configure('title', font=('楷体', 20, 'bold'),
                            foreground='red', justify=CENTER, spacing3=20)
        text2.tag_configure('detail', foreground='darkgray',
                            font=('微软雅黑', 11, 'bold'),
                            spacing2=10,  # 设置行间距
                            spacing3=15)  # 设置段间距
        text2.insert(END, '\n')
        # 插入文本内容，设置使用 title 样式
        text2.insert(END, '疯狂 Java 讲义\n', 'title')
        # 创建图片
        star = PhotoImage(file='images/g016.gif')
        text2.bm = star
        details = ('《疯狂 Java 讲义》历时十年沉淀，现以升级到第 4 版，' + \
                   '经过无数 Java 学习者的反复验证，被包括北京大学在内的大量 985、' + \
                   '211 高校的优秀教师引荐为参考子良，选作题材。\n',
                   '《疯狂 Java 讲义》曾被翻译为中文繁体字版，在中国台湾上市发行。\n',
                   '《疯狂 Java 讲义》屡获殊荣，多次获取电子工业出版社的“畅销图书”' + \
                   '“畅销图书”奖项，作者本人也多次获得“优秀作者”的称号。' + \
                   '仅第 3 版一版的印量即达 9 万多册。\n')
        # 采用循环插入多条介绍信息
        for de in details:
            text2.image_create(END, image=star)
            text2.insert(END, de, 'detail')
        url = ['https://item.jd.com/12261787.html', 'http://product.dangdang.com/23532609.html']
        name = ['京东链接', '当当链接']
        m = 0
        for each in name:
            # 为每个链接创建单独的配置
            text2.tag_configure(m, foreground='blue', underline=True,
                                font=('微软雅黑', 13, 'bold'))
            text2.tag_bind(m, '<Enter>', self.show_arrow_cursor)
            text2.tag_bind(m, '<Leave>', self.show_common_cursor)
            # 使用 handlerAdaptor 包装，将当前链接参数传入事件处理方法中
            text2.tag_bind(m, '<Button-1>', self.handlerAdaptor(self.click, x=url[m]))
            text2.insert(END, each + '\n', m)
            m += 1

    def show_arrow_cursor(self, event):
        # 光标移上去时变成箭头
        self.text.config(cursor='arrow')

    def show_common_cursor(self, event):
        # 光标移出去时恢复原样
        self.text.config(cursor='xterm')

    def click(self, event, x):
        import webbrowser
        # 使用默认浏览器打开链接
        webbrowser.open(x)

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


root = Tk()
root.title('Text 测试')
App(root)
root.mainloop()
