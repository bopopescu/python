# 导入访问 MySQL 的模块
import mysql.connector

# ①、连接数据库
conn = mysql.connector.connect(user='root', password='123456',
                               host='192.168.75.102', port='3306',
                               database='python', use_unicode=True,
                               charset='utf8')
# ②、获取游标
c = conn.cursor()
# ③、执行 DDL 语句创建数据表
c.execute('''create table user_tb(
	user_id int primary key auto_increment,
	name varchar(255),
	pass varchar(255), 
	gender varchar(255))''')
# 执行 DDL 语句创建数据表
c.execute('''create table order_tb(
	order_id integer primary key auto_increment,
	item_name varchar(255),
	item_price double,
    item_number double,
	user_id int,
    foreign key(user_id) references user_tb(user_id) )''')
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
