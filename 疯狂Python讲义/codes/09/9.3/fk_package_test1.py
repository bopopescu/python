# 导入fk_package包，实际上就是导入包下的__init__.py文件
import fk_package
# 导入fk_package包下的print_shape模块
# 实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape
# 导入fk_package包下的billing模块
# 实际上就是导入fk_package目录下的billing.py
from fk_package import billing
# 导入fk_package包下的arithmetic_chart模块
# 实际上就是导入fk_package目录下的arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)
