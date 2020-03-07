import unittest

from hello import *


class TestHello(unittest.TestCase):
    # 测试 say_hello 函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World.")

    # 测试 add 函数
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)

    @classmethod
    def setUpClass(cls):
        print('\n====执行 setUpClass 在类级别模拟初始化固件====')

    @classmethod
    def tearDownClass(cls):
        print('\n====调用 tearDownClass 在类级别模拟销毁固件====')
