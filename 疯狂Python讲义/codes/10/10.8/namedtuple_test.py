from collections import namedtuple

# 定义命名元组类：Point
Point = namedtuple('Point', ['x', 'y'])
# 初始化 Point 对象，既可用位置参数，也可用命名参数
p = Point(11, y=22)
# 像普通元组一样根据索引访问元素
print(p[0] + p[1])
# 执行元组解包，按元素的位置解包
a, b = p
print(a, b)
# 根据字段名访问各元素
print(p.x + p.y)
print(p)
my_data = ['East', 'North']
# 创建命名元素对象
p2 = Point._make(my_data)
print(p2)
# 替换命名元组对象的字段值
p2._replace(y='South')
print(p2)
# 输出 p2 包含的所有字段
print(p2._fields)
# 定义一个命名元组类
Color = namedtuple('Color', 'red green blue')
# 再定义一个命名元组类，其字段由 Point 的字段加上 Color 的字段组成
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
# 创建 Pixel 对象，分别为 x、y、red、green、blue 字段赋值
pix = Pixel(11, 22, 128, 255, 0)
print(pix)
