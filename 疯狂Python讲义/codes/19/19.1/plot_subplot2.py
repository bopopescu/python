import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
# 定义从 -pi 到 pi 之间的数据，平均取 64 个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①
# 将整个 figure 分成两行一列，第三个参数表示该图形放在第 1 个网格
plt.subplot(2, 1, 1)
# 绘制正弦曲线
plt.plot(x_data, np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线')

# 将整个 figure 分成两行两列，并将该图形放在第 4 个网格
plt.subplot(223)
# 绘制余弦曲线
plt.plot(x_data, np.cos(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('余弦曲线')

# 将整个 figure 分成两行两列，并该图形放在第 4 个网格
plt.subplot(224)
# 绘制正切曲线
plt.plot(x_data, np.tan(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正切曲线')

plt.show()
