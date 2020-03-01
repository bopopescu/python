import os

# 判断当前目录的权限
ret = os.access('../1', os.F_OK | os.R_OK | os.W_OK | os.X_OK)
print("os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:", ret)
# 判断 os.access_test.py 文件的权限
ret = os.access('os.access_test.py', os.F_OK | os.R_OK | os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)
