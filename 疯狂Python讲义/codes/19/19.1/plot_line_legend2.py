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
# 调用 show() 函数显示图形
plt.show()
