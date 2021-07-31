#  -*- coding:utf-8 -*-
import unittest

from uiautomator import device as d


class Mytest(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        print("--------------初始化工作")

    # 退出清理工作
    def tearDown(self):
        print("--------------退出清理工作")

    # 测试点击猫宁考勤case
    def test_login(self):
        d(text="猫宁考勤").click()
        print("--------------测试1")

    # 测试2
    def test_z(self):
        print("--------------测试2")  # 这里你可以写你的第二个测试用例，

    # 测试3
    def test_w(self):
        print("--------------测试3")  # 这里你可以写你的第三个测试用例。。。。。。。。。。。。。


if __name__ == '__main__':
    unittest.main()
