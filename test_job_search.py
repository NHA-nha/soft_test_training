# 导入pytest和selenium库
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 定义一个测试类
class TestLagou:

    # 定义一个fixture方法，用于初始化浏览器驱动和网址
    @pytest.fixture(scope="class")
    def setup(self):
        # 创建一个Chrome浏览器驱动对象
        self.driver = webdriver.Edge()
        # 打开被测网站
        self.driver.get("https://www.lagou.com/")
        # 最大化窗口
        self.driver.maximize_window()
        # 等待3秒
        self.driver.implicitly_wait(3)
        # 返回驱动对象
        return self.driver

    # 定义一个参数化的测试方法，用于搜索不同的职位和地点
    @pytest.mark.parametrize("job, location",
                             [("软件测试", "北京"), ("软件测试", "上海"), ("软件测试", "深圳"), ("软件测试", "广州"),
                              ("测试开发", "北京"), ("测试开发", "上海"), ("测试开发", "深圳"), ("测试开发", "广州")])
    def test_search(self, setup, job, location):
        # 调用fixture方法，获取驱动对象
        driver = setup
        time.sleep(5)
        element = driver.find_element(By.ID, "cboxClose")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(5)
        # 定位首页的搜索框，并输入职位名称
        driver.find_element_by_id("search_input").send_keys(job)
        # 定位下拉列表，并选择工作地点
        driver.find_element_by_css_selector(f"li[data-val='{location}']").click()
        # 定位搜索按钮，并点击
        driver.find_element_by_id("search_button").click()
        # 切换到新打开的窗口
        driver.switch_to.window(driver.window_handles[-1])
        # 定位筛选栏中的应届选项，并点击
        driver.find_element_by_css_selector("li[data-lg-tj-id='8E00'][data-lg-tj-no='0001']").click()
        # 定位排序栏中的最新选项，并点击
        driver.find_element_by_css_selector("li[data-lg-tj-id='8F00'][data-lg-tj-no='0001']").click()
        # 获取职位列表中的第一个职位名称
        first_job = driver.find_element_by_css_selector("h3.position-name > a").text
        # 获取职位列表中的第一个职位发布时间
        first_time = driver.find_element_by_css_selector("span.format-time").text
        # 打印职位名称和发布时间
        print(f"Job: {first_job}, Time: {first_time}")
        # 断言职位名称包含搜索的关键词
        assert job in first_job
