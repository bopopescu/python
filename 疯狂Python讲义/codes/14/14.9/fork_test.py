import os

print('父进程（%s）开始执行' % os.getpid())
# 开始 fork 一个子进程
# 从这行代码开始，下面代码都会被两个进程执行
pid = os.fork()
print('进程进入：%s' % os.getpid())
# 如果 pid 为 0，表明子进程
if pid == 0:
    print('子进程，其 ID 为 (%s)， 父进程 ID 为 (%s)' % (os.getpid(), os.getppid()))
else:
    print('我 (%s) 创建的子进程 ID 为 (%s).' % (os.getpid(), pid))
print('进程结束：%s' % os.getpid())
