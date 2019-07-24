class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1
        # return self返回调用该方法的对象
        return self


rs = ReturnSelf()
# 可以连续调用同一个方法
rs.grow().grow().grow()
print('rs的age属性值是：', rs.age)
