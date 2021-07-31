import unittest


class TestCaseDemo(unittest.TestCase):
    def testassertdemo(self):
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(1, [2, 3, 4])
        self.assertEqual('1', '1')
        self.assertNotEqual(1, 2)
        self.assertTrue(2 == 2)

    def testassertdemo_1(self):
        self.assertDictEqual({"code": 1}, {"code": 1})
        self.assertListEqual([1, 2], [1, 2])
        self.assertMultiLineEqual("name", "name")

    def testassertdemo_2(self):
        self.assertGreater(2, 0)
        self.assertGreaterEqual(2, 0)
        self.assertNotRegex("1", "122")  # 正则是否匹配
        self.assertCountEqual("12", "12")


# 1、第一种方法，一条一条case加载用例
def suite():
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    case1 = TestCaseDemo("testassertdemo")
    suite.addTest(case1)

    case2 = TestCaseDemo("testassertdemo_1")
    suite.addTest(case2)

    case3 = TestCaseDemo("testassertdemo_2")
    suite.addTest(case3)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
