import csv

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建 csv 文件读取器
    reader = csv.reader(f)
    # 读取第一行，这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 读取第二行，这行是真正的数据。
    first_row = next(reader)
    print(first_row)
