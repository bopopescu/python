from collections import deque

q = deque(('Kotlin', 'Python'))
# 元素入队列
q.append('Erlang')
q.append('Swift')
print('q 中的元素：', q)
# 元素出队列，先添加的元素先出队列
print(q.popleft())
print(q.popleft())
print(q)
