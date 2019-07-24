class Dog:
    # 定义一个jump()方法
    def jump(self):
        print('正在执行jump方法')

    # 定义一个run()方法，run()方法需要借助jump()方法
    def run(self):
        # 使用self参数引用调用run()方法的对象
        self.jump()
        print('正在执行run方法')


dog = Dog()
dog.run()
