# 导入访问 SQLite 的模块
import sqlite3


# 先定义一个普通函数，准备注册为 SQL 中的自定义函数
def reverse_ext(st):
    # 对字符串反转，前后加方括号
    return '[' + st[::-1] + ']'


# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 调用 create_function 注册自定义函数：enc
conn.create_function('enc', 1, reverse_ext)
# ②、获取游标
c = conn.cursor()
# ③、在SQL语句中使用enc自定义函数
c.execute('insert into user_tb values(null, ?, enc(?), ?)',
          ('贾宝玉', '123456', 'male'))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
