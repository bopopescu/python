# 导入访问 MySQL 的模块
import mysql.connector

# ①、连接数据库
conn = mysql.connector.connect(user='root', password='123456',
                               host='192.168.75.102', port='3306',
                               database='python', use_unicode=True,
                               charset='utf8')
# 将 autocommit 设置 True，关闭事务
conn.autocommit = True
# ②、获取游标
c = conn.cursor()
# ③、调用执行 insert 语句插入数据
c.execute('insert into user_tb values(null, %s, %s, %s)',
          ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null, %s, %s, %s, %s)',
          ('鼠标', '34.2', '3', 1))
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
