import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 定义 2 个列表分别作为 X 轴、Y 轴数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# 第一个列表代表横坐标的值，第二个代表纵坐标的值
# plt.plot(x_data, y_data)
plt.plot(y_data)
# 调用 show() 函数显示图形
plt.show()
