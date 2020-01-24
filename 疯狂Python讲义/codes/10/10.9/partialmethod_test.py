from functools import *


class Cell:
    def __init__(self):
        self._alive = False

    # @property 装饰器指定该方法可使用属性语法访问
    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    # 指定 set_alive() 方法，就是将 set_sate() 方法的 state 参数指定为 True
    set_alive = partialmethod(set_state, True)
    # 指定 set_dead() 方法，就是将 set_state() 方法的 state 参数指定为 False
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)
# 相当于调用 c.set_state(True)
c.set_alive()
print(c.alive)
# 相当于调用 c.set_state(False)
c.set_dead()
print(c.alive)
