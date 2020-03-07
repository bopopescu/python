# 导入访问 MySQL 的模块
import mysql.connector


def query_db():
    # ①、连接数据库
    conn = mysql.connector.connect(user='root', password='123456',
                                   host='192.168.75.102', port='3306',
                                   database='python', use_unicode=True,
                                   charset='utf8')
    # ②、获取游标
    c = conn.cursor()
    # ③、调用执行 select 语句查询数据
    c.execute('select * from user_tb where user_id > %s', (2,))
    # 通过游标的 description 属性获取列信息
    description = c.description
    # 使用 fetchall 获取游标中的所有结果集
    rows = c.fetchall()
    # ④、关闭游标
    c.close()
    # ⑤、关闭连接
    conn.close()
    return description, rows
