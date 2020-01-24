from collections import defaultdict

my_dict = {}
# 使用 int 作为 defaultdict 的 default_factory
# 当 key 不存在时，将会返回 int 函数的返回值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a'])
print(my_dict['a'])
