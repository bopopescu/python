# 导入访问 SQLite 的模块
import sqlite3


# 去掉字符串第一个、最后一个字符后比较大小
def my_collate(st1, st2):
    if st1[1: -1] == st2[1: -1]:
        return 0
    elif st1[1: -1] > st2[1: -1]:
        return 1
    else:
        return -1


# ①、打开或创建数据库
# 也可以使用特殊名：:memory: 代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 调用 create_collation 注册自定义比较函数：sub_cmp
conn.create_collation('sub_cmp', my_collate)
# ②、获取游标
c = conn.cursor()
# ③、在 SQL 语句中使用 sub_cmp 自定义的比较函数
c.execute('select * from user_tb order by pass collate sub_cmp')
# 采用 for-in 循环遍历游标
for row in c:
    print(row)
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
