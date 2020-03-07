import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义 2 个列表分别作为两条折线的 Y 轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color='red', linewidth=2.0,
         linestyle='--', label='疯狂Java讲义年销量')
plt.plot(x_data, y_data2, color='blue', linewidth=3.0,
         linestyle='-.', label='疯狂Android讲义年销量')
import matplotlib.font_manager as fm

# 使用 Matplotlib 的字体管理器加载中文字体
my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
# 调用 legend 函数设置图例
plt.legend(loc='best')
# 设置两条坐标轴的名字
plt.xlabel("年份")
plt.ylabel("图书销量（本）")
# 设置数据图的标题
plt.title('疯狂图书的历年销量')
# 设置 Y 轴上的刻度值
# 第一个参数是点的位置，第二个参数是点的文字提示
plt.yticks([50000, 70000, 100000],
           [r'挺好', r'优秀', r'火爆'])
ax = plt.gca()
# 设置将 X 轴的刻度值放在底部  X轴上
ax.xaxis.set_ticks_position('bottom')
# 设置将 Y 轴的刻度值放在底部 X 轴上
ax.yaxis.set_ticks_position('left')
# 设置右边坐标轴线的颜色（设置为 none 表示不显示）
ax.spines['right'].set_color('none')
# 设置顶部坐标轴线的颜色（设置为 none 表示不显示）
ax.spines['top'].set_color('none')
# 定义底部坐标轴线的位置（放在 70000 数值处）
ax.spines['bottom'].set_position(('data', 70000))
# 调用 show() 函数显示图形
plt.show()
