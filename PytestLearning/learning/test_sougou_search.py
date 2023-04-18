from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test():
    # 前提条件
    def setup_method(self,method):
        self.driver = webdriver.Edge()
        self.vars={}
    # 后置动作
    def teardown_method(self,method):
        self.driver.quit()
    # 测试用例步骤
    def test_sougou_search(self):
        # 打开网页
        self.driver.get("https://www.sogou.com")
        self.driver.set_window_size(1235,693)
        # 输入搜索内容
        self.driver.find_element(By.ID,"query").click()
        self.driver.find_element(By.ID,"query").send_keys("霍格沃兹测试开发")
        # 点击搜索
        self.driver.find_element(By.ID,"stb").click()
        element = self.driver.find_element(By.ID,"stb")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 添加断言信息，判断搜索列表中，是否含有”霍格沃兹测试开发“
        res_element = self.driver.find_element(By.CSS_SELECTOR,"#sogou_vr_30000000_0 > em")
        # 获取到定位的文本信息
        # 判断实际获取到的搜索展示的列表和䰴的是否一致
        assert res_element.text == "霍格沃兹测试开发"
