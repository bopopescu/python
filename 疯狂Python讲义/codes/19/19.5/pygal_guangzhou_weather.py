import csv
import pygal

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建 csv 文件读取器
    reader = csv.reader(f)
    # 读取第一行，这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 准备展示的数据
    shades, sunnys, cloudys, rainys = 0, 0, 0, 0
    for row in reader:
        if '阴' in row[3]:
            shades += 1
        elif '晴' in row[3]:
            sunnys += 1
        elif '云' in row[3]:
            cloudys += 1
        elif '雨' in row[3]:
            rainys += 1
        else:
            print(rows[3])
# 创建 pygal.Pie 对象（饼图）
pie = pygal.Pie()
# 为饼图添加数据
pie.add("阴", shades)
pie.add("晴", sunnys)
pie.add("多云", cloudys)
pie.add("雨", rainys)
pie.title = '2017 年广州天气汇总'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 指定将数据图输出到 SVG 文件中
pie.render_to_file('guangzhou_weather.svg')
