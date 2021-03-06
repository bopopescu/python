import json
from matplotlib import pyplot as plt
import numpy as np

filename = 'gdp_json.json'
# 读取 JSON 格式的 GDP 数据
with open(filename) as f:
    gpd_list = json.load(f)
# 使用 list 列表依次保存中国、美国、日本、俄罗斯、加拿大的GDP值
country_gdps = [{}, {}, {}, {}, {}]
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
# 遍历列表的每个元素，每个元素是一个 GDP 数据项
for gpd_dict in gpd_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gpd_dict['Country Code'] == country_code:
            year = gpd_dict['Year']
            # 只读取 2001 年到 2016
            if 2017 > year > 2000:
                country_gdps[i][year] = gpd_dict['Value']
# 使用 list 列表依次保存中国、美国、日本、俄罗斯、加拿大的 GDP 值
country_gdp_list = [[], [], [], [], []]
# 构建时间数据
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        # 除以 1e8，让数值变成以亿为单位
        country_gdp_list[i].append(country_gdps[i][year] / 1e8)
bar_width = 0.15
fig = plt.figure(dpi=128, figsize=(15, 8))
colors = ['indianred', 'steelblue', 'gold', 'lightpink', 'seagreen']
# 定义国家名称列表
countries = ['中国', '美国', '日本', '俄罗斯', '加拿大']
# 采用循环绘制 5 组柱状图
for i in range(len(colors)):
    # 使用自定义 X 坐标将数据分开
    plt.bar(x=np.arange(len(x_data)) + bar_width * i, height=country_gdp_list[i],
            label=countries[i], color=colors[i], alpha=0.8, width=bar_width)
    # 仅为中国、美国的条柱上绘制 GDP 数值
    if i < 2:
        for x, y in enumerate(country_gdp_list[i]):
            plt.text(x, y + 100, '%.0f' % y, ha='center', va='bottom')
# 为 X 轴设置刻度值
plt.xticks(np.arange(len(x_data)) + bar_width * 2, x_data)
# 设置标题
plt.title("2001 到 2016 年各国 GDP 对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("GDP(亿美元)")
# 显示图例
plt.legend()
plt.show()
