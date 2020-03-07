import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
# 定义从 -pi 到 pi 之间的数据，平均取 64 个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①

# 将绘图区域分成 2 行 3 列
gs = gridspec.GridSpec(2, 3)
# 指定 ax1 占用第一行（0）整行
ax1 = plt.subplot(gs[0, :])
# 指定 ax1 占用第二行（1）的第一格（第二个参数 0 代表）
ax2 = plt.subplot(gs[1, 0])
# 指定 ax1 占用第二行（1）的第二、三格（第二个参数 0 代表）
ax3 = plt.subplot(gs[1, 1:3])

# 绘制正弦曲线
ax1.plot(x_data, np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')

# 绘制余弦曲线
ax2.plot(x_data, np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('余弦曲线')

# 绘制正切曲线
ax3.plot(x_data, np.tan(x_data))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')

plt.show()
