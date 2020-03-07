import pygal

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992,
        0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
          'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
          'SQL', 'Assembly langugage', '其他']
# 创建 pygal.Gauge 对象（仪表图）
gauge = pygal.Gauge()
gauge.range = [0, 1]
# 采用循环为仪表图添加数据
for i, per in enumerate(data):
    gauge.add(labels[i], per)
gauge.title = '2018 年 8 月编程语言'
# 设置将图例放在底部
gauge.legend_at_bottom = True
# 指定将数据图输出到 SVG 文件中
gauge.render_to_file('language_percent.svg')
