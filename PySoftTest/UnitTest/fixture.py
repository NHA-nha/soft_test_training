import unittest


class TextLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("打开网址")

    def tearDown(self) -> None:
        print("关闭网址")

    def test_method1(self):
        print('测试方法 1-1')

    def test_method2(self):
        print('测试方法 1-2')

    @classmethod
    def setUpClass(cls) -> None:
        print("打开浏览器----1")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器----5")
