import pygal

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992,
        0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
          'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
          'SQL', 'Assembly langugage', '其他']
# 创建 pygal.Pie 对象（饼图）
pie = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)
pie.title = '2018 年 8 月编程语言'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 设置内圈的半径长度
pie.inner_radius = 0.4
# 创建半圆数据图
pie.half_pie = True
# 指定将数据图输出到 SVG 文件中
pie.render_to_file('language_percent.svg')
