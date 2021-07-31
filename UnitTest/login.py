#  -*- coding:utf-8 -*-
import time
import unittest

import uiautomator2 as u2


class Mytest(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        print("--------------初始化工作")

    # 退出清理工作
    def tearDown(self):
        print("--------------退出清理工作")

    # 测试登录
    def test_login(self):
        d = u2.connect('192.168.5.101:5555')
        # 停止应用
        d.app_stop('com.upchina.teach')
        time.sleep(3)
        # 打开应用
        d.app_start('com.upchina.teach')
        # 自动跳过弹出窗口
        # d.disable_popups()
        # 点击首页头像
        d(resourceId="com.upchina.teach:id/home_mine_icon").wait()
        d(resourceId="com.upchina.teach:id/home_mine_icon").click()
        # 点击头像
        d(resourceId="com.upchina.teach:id/user_mine_head").wait()
        d(resourceId="com.upchina.teach:id/user_mine_head").click()
        # 点击账号密码登录
        d(resourceId="com.upchina.teach:id/up_user_login_segment_pwd").wait()
        d(resourceId="com.upchina.teach:id/up_user_login_segment_pwd").click()
        time.sleep(1)
        # 输入账号
        d(resourceId="com.upchina.teach:id/up_user_edit_text_view_input").set_text('llf991225')
        time.sleep(1)
        # 输入密码
        d(resourceId="com.upchina.teach:id/up_user_password_edit").set_text('123456')
        time.sleep(1)
        # 同意隐私政策
        d(resourceId="com.upchina.teach:id/up_user_login_checkbox").click()
        time.sleep(1)
        # 点击登录按钮
        d(resourceId="com.upchina.teach:id/up_user_login_btn").click()
        time.sleep(1)
        print("--------------测试1")


if __name__ == '__main__':
    unittest.main()
