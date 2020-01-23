from collections import deque

q = deque(range(5))
print('q 中的元素：', q)
# 执行旋转，使之首尾相连
q.rotate()
print('q 中的元素：', q)
# 再次执行旋转，使之首尾相连
q.rotate()
print('q 中的元素：', q)
