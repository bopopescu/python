# 导入访问 SQLite 的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用 executemany() 方法把同一条 SQL 语句执行多次
c.executemany('update user_tb set name=? where _id=?',
              (('小孙', 2),
               ('小白', 3),
               ('小猪', 4),
               ('小牛', 5),
               ('小唐', 6)))
# 通过 rowcount 获取被修改的记录条数
print('修改的记录条数：', c.rowcount)
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
