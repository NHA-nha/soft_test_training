"""
参数化时，避免出现乱码
"""
from typing import List


# 修改测试用例名称中文编码，utf-8转为unicode
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
