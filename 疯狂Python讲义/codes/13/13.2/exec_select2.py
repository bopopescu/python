# 导入访问 SQLite 的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用执行 select 语句查询数据
c.execute('select * from user_tb where _id > ?', (2,))
# 通过游标的 description 属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 每次抓取 3 条记录，该方法返回一个由 3 条记录组成的列表
    rows = c.fetchmany(3)
    # 如果抓取的 rows 为 None，退出循环
    if not rows:
        break
    # 再次使用循环遍历获取的列表
    for r in rows:
        print(r)
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
