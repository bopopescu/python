# 导入访问 SQLite 的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用 executescript() 方法执行一段 SQL 脚本
c.executescript('''
    insert into user_tb values(null, '武松', '3444', 'male');  
    insert into user_tb values(null, '林冲', '44444', 'male');
    create table item_tb(_id integer primary key autoincrement,
	name,
	price);
    ''')
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
