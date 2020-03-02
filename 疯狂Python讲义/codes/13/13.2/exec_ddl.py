# 导入访问 SQLite 的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、执行 DDL 语句创建数据表
c.execute('''create table user_tb(
	_id integer primary key autoincrement,
	name text,
	pass text, 
	gender text)''')
# 执行 DDL 语句创建数据表
c.execute('''create table order_tb(
	_id integer primary key autoincrement,
	item_name text,
	item_price real,
    item_number real,
	user_id inteter,
    foreign key(user_id) references user_tb(_id) )''')
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
