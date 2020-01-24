from functools import *


@total_ordering
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User[name=%s]' % self.name

    def _is_valid_operand(self, other):
        return hasattr(other, 'name')

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.name.lower() == other.lastname.lower()

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.lastname.lower() < other.lastname.lower()


# 打印被装饰之后的 User 类中的 __gt__ 方法
print(User.__gt__)
