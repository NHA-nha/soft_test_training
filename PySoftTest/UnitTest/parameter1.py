import json
import unittest

from parameterized import parameterized

from tools import login


def build_data():
    with open("data.json", encoding="utf-8") as f:
        result = json.load(f)
        data = []  # [(),()]
        for i in result:
            data.append((i.get('username'), i.get('password'), i.get('expect')))
    return data


class TestLogin(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))
