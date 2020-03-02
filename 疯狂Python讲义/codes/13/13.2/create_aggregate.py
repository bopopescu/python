# 导入访问 SQLite 的模块
import sqlite3


# 先定义一个普通类，准备注册为 SQL 中的自定义聚集函数
class MinLen:
    def __init__(self):
        self.min_len = None

    def step(self, value):
        # 如果 self.min_len 还未赋值，直接将当前 value 赋值给 self.min_lin
        if self.min_len is None:
            self.min_len = value
            return
        # 找到一个长度更短的 value，用 value 代替 self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value

    def finalize(self):
        return self.min_len


# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 调用 create_aggregate 注册自定义聚集函数：min_len
conn.create_aggregate('min_len', 1, MinLen)
# ②、获取游标
c = conn.cursor()
# ③、在SQL语句中使用 min_len 自定义聚集函数
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
