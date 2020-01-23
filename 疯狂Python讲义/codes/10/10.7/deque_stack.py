from collections import deque

stack = deque(('Kotlin', 'Python'))
# 元素入栈
stack.append('Erlang')
stack.append('Swift')
print('stack 中的元素：', stack)
print(stack.pop())
print(stack.pop())
print(stack)
