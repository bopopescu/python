# 导入访问 SQLite 的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用 executemany() 方法把同一条 SQL 语句执行多次
c.executemany('insert into user_tb values(null, ?, ?, ?)',
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
