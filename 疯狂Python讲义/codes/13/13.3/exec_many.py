# 导入访问 MySQL 的模块
import mysql.connector

# ①、连接数据库
conn = mysql.connector.connect(user='root', password='123456',
                               host='192.168.75.102', port='3306',
                               database='python', use_unicode=True,
                               charset='utf8')
# ②、获取游标
c = conn.cursor()
# ③、调用 executemany() 方法把同一条SQL语句执行多次
c.executemany('insert into user_tb values(null, %s, %s, %s)',
              (('sun', '123456', 'male'),
               ('bai', '123456', 'female'),
               ('zhu', '123456', 'male'),
               ('niu', '123456', 'male'),
               ('tang', '123456', 'male')))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
