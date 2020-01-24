from collections import ChainMap
import builtins

my_name = '孙悟空'


def test():
    my_name = 'yeeku'
    # 将 locals、globals、builtins 的变量链成 ChainMap
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    # 访问 my_name 对应的 value，优先使用局部范围的定义
    print(pylookup['my_name'])
    # 访问 len 对应的 value，由于在局部范围、全局范围中都找不到，因此访问内置定义的len函数
    print(pylookup['len'])


test()
