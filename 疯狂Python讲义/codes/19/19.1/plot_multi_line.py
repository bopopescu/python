import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义 2 个列表分别作为两条折线的 Y 轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 传入 2 组分别代表 X 轴、Y 轴的数据
# plt.plot(x_data, y_data, x_data, y_data2)
plt.plot(x_data, y_data)
plt.plot(x_data, y_data2)
# 调用 show() 函数显示图形
plt.show()
