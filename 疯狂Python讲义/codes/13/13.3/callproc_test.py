'''
create procedure add_pro(a int, b int, out sum int)
begin
set sum = a + b;
end;
'''
# 导入访问 MySQL 的模块
import mysql.connector

# ①、连接数据库
conn = mysql.connector.connect(user='root', password='123456',
                               host='192.168.75.102', port='3306',
                               database='python', use_unicode=True,
                               charset='utf8')
# ②、获取游标
c = conn.cursor()
# ③、调用 callproc() 方法执行存储过程
# 虽然 add_pro 存储过程需要 3 个参数，但最后一个参数是传出参数，
# 因此程序不会用它的值
result_args = c.callproc('add_pro', (5, 6, 0))
# 返回的 result_args 既包含了传入参数的值，也包含了传出参数的值
print(result_args)
# 如果只想访问传出参数的值，可直接访问 result_args 的第 3 个元素，如下代码
print(result_args[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
