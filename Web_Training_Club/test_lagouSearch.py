from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLagouSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_lagouSearch(self):
        self.driver.get("https://www.lagou.com/")
        self.driver.set_window_size(1361, 730)
        self.driver.find_element(By.ID, "cboxClose").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, "search_input").click()
        self.driver.find_element(By.ID, "search_input").send_keys("软件测试")
        self.driver.find_element(By.ID, "search_button").click()
        self.driver.find_element(By.CLASS_NAME, "active__YmPJe").click()  # 点击“最新”

        res_element1 = self.driver.find_element(By.ID, "jobList")
        assert '测试' in res_element1.text
