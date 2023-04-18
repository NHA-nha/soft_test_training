import unittest

from parameterized import parameterized

from tools import login

data = [
    ('admin', '123456', '登陆成功'),
    ('root', '123456', '登陆失败'),
    ('admin', '123123', '登陆失败')
]


class TestLogin(unittest.TestCase):
    @parameterized.expand(data)
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))
