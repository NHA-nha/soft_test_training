# 结合pytest框架
# 用例标题 = 文件名+类名+方法名
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:
    def setup(self):
        # 前提条件：进入测试人论坛的搜索页面
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(3)
        self.driver.get("https://ceshiren.com/search?expanded=true")

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']").send_keys("appium")
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # 获取实际结果，即为获取搜索列表的标题内容
        # 1.第一种方式，获取第一个搜索结果
        time.sleep(3)  # 加一个3秒的强制等待，等待页面渲染完成，如果没有报错，证明定位成功
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        # 获取文本的实际结果 断言，appium关键字是否在获取的实际结果文本中
        assert "appium" in web_element.text.lower()
