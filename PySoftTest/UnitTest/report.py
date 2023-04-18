import unittest
from HTMLTestRunner_py3 import HTMLTestRunner

'''
stream=sys.stdout, # 必填，open对象，注意用 wb 打开
verbosity=1, # 可选，报告详细程度，默认 1 简略，2 详细
title=None, #可选，测试报告的标题
description=None # 可选，描述信息，python版本，pycharm版本
'''
suite = unittest.defaultTestLoader.discover('..', 'parameter1.py')

file = 'report.html'
with open(file, 'wb') as f:
    runner = HTMLTestRunner(f, 2, "测试报告", "python 3.8")
    runner.run(suite)
