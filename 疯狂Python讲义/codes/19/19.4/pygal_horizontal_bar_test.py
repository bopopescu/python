import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建 pygal.HorizontalBar 对象（水平柱状图）
horizontal_bar = pygal.HorizontalBar()
# 添加两组数据
horizontal_bar.add('疯狂 Java 讲义', y_data)
horizontal_bar.add('疯狂 Android 讲义', y_data2)
# 设置 Y 轴（确实如此）的刻度值
horizontal_bar.x_labels = x_data
# 重新设置 X 轴（确实如此）的刻度值
horizontal_bar.y_labels = [20000, 40000, 60000, 80000, 100000]
horizontal_bar.title = '疯狂图书的历年销量'
# 设置 X、Y 轴的标题
horizontal_bar.x_title = '销量'
horizontal_bar.y_title = '年份'
# 设置将图例放在底部
horizontal_bar.legend_at_bottom = True
# 指定将数据图输出到 SVG 文件中
horizontal_bar.render_to_file('fk_books.svg')
