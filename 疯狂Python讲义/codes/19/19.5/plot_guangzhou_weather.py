import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建 csv 文件读取器
    reader = csv.reader(f)
    # 读取第一行，这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 定义读取起始日期
    start_date = datetime(2017, 6, 30)
    # 定义结束日期
    end_date = datetime(2017, 8, 1)
    # 定义 3 个 list 列表作为展示的数据
    dates, highs, lows = [], [], []
    for row in reader:
        # 将第一列的值格式化为日期
        d = datetime.strptime(row[0], '%Y-%m-%d')
        # 只展示 2017 年 7 月的数据
        if start_date < d < end_date:
            dates.append(d)
            highs.append(int(row[1]))
            lows.append(int(row[2]))

# 配置图形
fig = plt.figure(dpi=128, figsize=(12, 9))
# 绘制最高气温的折线
plt.plot(dates, highs, c='red', label='最高气温',
         alpha=0.5, linewidth=2.0, linestyle='-', marker='v')
# 再绘制一条折线
plt.plot(dates, lows, c='blue', label='最低气温',
         alpha=0.5, linewidth=3.0, linestyle='-.', marker='o')
# 为两个数据的绘图区域填充颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置标题
plt.title("广州 2017 年 7 月最高气温和最低气温")
# 为两条坐标轴设置名称
plt.xlabel("日期")
# 该方法绘制斜着的日期标签
fig.autofmt_xdate()
plt.ylabel("气温（℃）")
# 显示图例
plt.legend()
ax = plt.gca()
# 设置右边坐标轴线的颜色（设置为 none 表示不显示）
ax.spines['right'].set_color('none')
# 设置顶部坐标轴线的颜色（设置为 none 表示不显示）
ax.spines['top'].set_color('none')
plt.show()
