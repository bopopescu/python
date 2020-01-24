from collections import ChainMap
import os, argparse

# 定义默认参数
defaults = {'color': '蓝色', 'user': 'yeeku'}
# 创建程序参数解析器
parser = argparse.ArgumentParser()
# 为参数解析器添加 -u (--user) 和 -c (--color) 参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
# 解析运行程序的参数
namespace = parser.parse_args()
# 将程序参数转换成 dict
cmmand_line_args = {k: v for k, v in vars(namespace).items() if v}
# 将 cmmand_line_args（由程序参数解析而来）、os.environ（环境变量）、defaults 链成 ChainMap
combined = ChainMap(cmmand_line_args, os.environ, defaults)
# 获取 color 对应的 value
print(combined['color'])
# 获取 user 对应的 value
print(combined['user'])
# 获取 PYTHONPATH 对应的 value
print(combined['PYTHONPATH'])
