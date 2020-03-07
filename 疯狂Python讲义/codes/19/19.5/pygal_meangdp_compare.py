import json
import pygal

filename = 'gdp_json.json'
# 读取 JSON 格式的 GDP 数据
with open(filename) as f:
    gpd_list = json.load(f)
pop_filename = 'population-figures-by-country.json'
# 读取 JSON 格式的人口数据
with open(pop_filename) as f:
    pop_list = json.load(f)

# 使用 list 列表依次保存美国、日本、俄罗斯、加拿大的人均 GDP 值
country_mean_gdps = [{}, {}, {}, {}]
country_codes = ['USA', 'JPN', 'RUS', 'CAN']
# 遍历列表的每个元素，每个元素是一个 GDP 数据项
for gpd_dict in gpd_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gpd_dict['Country Code'] == country_code:
            year = gpd_dict['Year']
            # 只读取 2001 年到 2016
            if 2017 > year > 2000:
                for pop_dict in pop_list:
                    # 获取指定国家的人口数据
                    if pop_dict['Country_Code'] == country_code:
                        # 使用该国 GDP 总值除以人口数量，得到人均 GDP
                        country_mean_gdps[i][year] = round(gpd_dict['Value']
                                                           / pop_dict['Population_in_%d' % year])
# 使用 list 列表依次保存美国、日本、俄罗斯、加拿大的人均 GDP 值
country_mean_gdp_list = [[], [], [], []]
# 构建时间数据
x_data = range(2001, 2017)
for i in range(len(country_mean_gdp_list)):
    for year in x_data:
        country_mean_gdp_list[i].append(country_mean_gdps[i][year])
# 定义国家名称列表
countries = ['美国', '日本', '俄罗斯', '加拿大']
# 创建 pygal.Bar 对象（柱状图）
bar = pygal.Bar()
# 采用循环添加代表条柱的数据
for i in range(len(countries)):
    bar.add(countries[i], country_mean_gdp_list[i])
bar.width = 1100
# 设置 X 轴的刻度值
bar.x_labels = x_data
bar.title = '2001 到 2016 年各国人均 GDP 对比'
# 设置 X、Y 轴的标题
bar.x_title = '年份'
bar.y_title = '人均 GDP (美元)'
# 设置 X 轴的刻度值旋转 45 度
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 指定将数据图输出到 SVG 文件中
bar.render_to_file('mean_gdp.svg')
