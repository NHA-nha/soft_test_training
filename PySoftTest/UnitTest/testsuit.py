import unittest

from UnitTest.case.testcase1 import TestDemo1
from UnitTest.case.testcase2 import TestDemo2

# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))
# 创建测试运行
runner = unittest.TextTestRunner()
# 运行
runner.run(suite)
