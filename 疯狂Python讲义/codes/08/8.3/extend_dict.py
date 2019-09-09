# 定义ValueDict类，继承dict类
class ValueDict(dict):
    # 定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类的构造函数
        super().__init__(*args, **kwargs)

    # 新增getkeys方法
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val: result.append(key)
        return result


my_dict = ValueDict(语文=92, 数学=89, 英语=92)
# 获取92对应的所有key
print(my_dict.getkeys(92))
my_dict['编程'] = 92
print(my_dict.getkeys(92))
