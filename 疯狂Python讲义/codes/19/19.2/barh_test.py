import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 构建数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3
# Y 轴数据使用 range(len(x_data), 就是 0、1、2...
plt.barh(y=range(len(x_data)), width=y_data, label='疯狂Java讲义',
         color='steelblue', alpha=0.8, height=bar_width)
# Y 轴数据使用 np.arange(len(x_data))+bar_width,
# 就是 bar_width、1+bar_width、2+bar_width... 这样就和第一个柱状图并列了
plt.barh(y=np.arange(len(x_data)) + bar_width, width=y_data2,
         label='疯狂 Android 讲义', color='indianred', alpha=0.8, height=bar_width)

# 在柱状图上显示具体数值, ha 参数控制水平对齐方式, va 控制垂直对齐方式
for y, x in enumerate(y_data):
    plt.text(x + 5000, y - bar_width / 2, '%s' % x, ha='center', va='bottom')
for y, x in enumerate(y_data2):
    plt.text(x + 5000, y + bar_width / 2, '%s' % x, ha='center', va='bottom')
# 为 Y 轴设置刻度值
plt.yticks(np.arange(len(x_data)) + bar_width / 2, x_data)
# 设置标题
plt.title("Java 与 Android 图书对比")
# 为两条坐标轴设置名称
plt.xlabel("销量")
plt.ylabel("年份")
# 显示图例
plt.legend()
plt.show()
