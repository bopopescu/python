import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

delta = 0.125
# 生成代表 X 轴数据的列表
x = np.arange(-3.0, 3.0, delta)
# 生成代表 Y 轴数据的列表
y = np.arange(-2.0, 2.0, delta)
# 对 x、y 数据执行网格化
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
# 计算 Z 轴数据（高度数据）
Z = (Z1 - Z2) * 2
# 绘制 3D 图形
ax.plot_surface(X, Y, Z,
                rstride=1,  # rstride（row）指定行的跨度
                cstride=1,  # cstride(column)指定列的跨度
                cmap=plt.get_cmap('rainbow'))  # 设置颜色映射
# 设置 Z 轴范围
ax.set_zlim(-2, 2)
# 设置标题
plt.title("3D 图")
plt.show()
