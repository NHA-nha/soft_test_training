import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 测试类
class TestCeshiren:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.vars = {}

    def setup_method(self):
        # 打开ceshiren网站
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1349, 717)

    def teardown_class(self):
        self.driver.quit()

    # 冒烟用例：搜索功能的正向测试
    def test_search(self):
        """
        搜索功能的正向测试,测试步骤
        1. 打开ceshiren网站
        2. 点击首页的搜索按钮
        3. 点击高级搜索按钮
        4. 输入搜索信息
        4. 点击搜索按钮
        6. 断言：搜索的信息和结果内容 一致/相关
        :return:
        """
        # 点击首页的搜索按钮
        self.driver.find_element(By.ID, "search-button").click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".searching").click()
        # 输入搜索信息
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys("selenium")
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # 隐式等待 全局
        self.driver.implicitly_wait(3)
        # 断言：搜索结果的文本中包含“selenium”
        assert "selenium" in self.driver.find_element(By.CSS_SELECTOR, ".topic-title").text

    # 截图，保存至allure报告
    def screenshot(self, name):
        # 截图
        self.driver.save_screenshot(f"{name}.png")
        # 塞入allure报告 使用命令行：pytest 文件名 --alluredir 目录名（./report）
        # 查看报告 命令：allure serve 报告名称（report）
        allure.attach.file(f"{name}.png", name="search-null", attachment_type=allure.attachment_type.PNG)

    # 异常场景：搜索内容为空
    def test_search_null(self):
        """
        测试步骤
        1. 打开ceshiren网站
        2. 点击首页的搜索按钮
        3. 点击高级搜索按钮
        4. 不输入搜索信息
        4. 点击搜索按钮
        6. 断言：搜索结果列表为空，提示：您的搜索内容过短。
        :return:
        """
        # 点击首页的搜索按钮
        self.driver.find_element(By.ID, "search-button").click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".searching").click()
        # 输入搜索信息
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys("")
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        try:
            search_text = self.driver.find_element(By.CSS_SELECTOR, ".fps-invalid").text
        except Exception:
            self.screenshot("search-special-characters-fail")
            raise AssertionError(f"Search results should be empty! Have created a new screenshot!")
        # 隐式等待 全局
        self.driver.implicitly_wait(3)
        # 断言：搜索结果的文本中包含“您的搜索词过短。”
        assert "您的搜索词过短。" == search_text

    # 异常场景：搜索内容为特殊字符
    @pytest.mark.parametrize("search_word", ["！@#@#@!", "西游记大闹红楼梦"])
    def test_search_special_characters(self, search_word):
        """
        测试步骤
        1. 打开ceshiren网站
        2. 点击首页的搜索按钮
        3. 点击高级搜索按钮
        4. 不输入搜索信息
        4. 点击搜索按钮
        6. 断言：搜索结果列表为空，提示：找不到结果。
        :return:
        """
        # 点击首页的搜索按钮
        self.driver.find_element(By.ID, "search-button").click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".searching").click()
        # 输入搜索信息：特殊字符
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys(search_word)
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        try:
            self.driver.implicitly_wait(3)
            search_text = self.driver.find_element(By.CSS_SELECTOR, ".search-results h3").text
        except Exception:
            self.screenshot("search-special-characters-fail")
            raise AssertionError(f"Search results for {search_word} are empty! Have created a new screenshot!")
        assert "找不到结果。" == search_text, f"Search results for {search_word} are not empty!"

    # 异常场景：搜索内容为超长字符,该内容的帖子存在
    @pytest.mark.parametrize("search_word", [
        "该图显示了客户端库与服务器通信,并传递了用来执行的每个Selenium命令.然后, "
        "服务器使用Selenium-Core的JavaScript命令将Selenium命令传递到浏览器.浏览器使用其JavaScript解释器执行Selenium命令.这将运行您在测试脚本中指定的Selenese"
        "操作或验证行为.Selenium 服务器Selenium 服务器从您的测试程序接收Selenium命令,对其进行解释,然后将运行这些测试的结果报告给您的程序.RC服务器捆绑了Selenium "
        "Core并将其自动注入浏览器.当您的测试程序打开浏览器(使用客户端库API函数)时,会发生这种情况.Selenium-Core是一个JavaScript程序,实际上是一组JavaScript函数,"
        "这些函数使用浏览器的内置JavaScript解释器来解释和执行Selenese命令.服务器使用简单的HTTP GET / "
        "POST请求从您的测试程序接收Selenese命令.这意味着您可以使用任何可以发送HTTP请求的编程语言来自动执行浏览器中的Selenium测试.客户端库客户端库提供了编程支持,"
        "使您可以从自己设计的程序中运行Selenium命令.每种受支持的语言都有一个不同的客户端库.Selenium客户端库提供了一个编程接口(API),即一组函数, 可从您自己的程序中运行Selenium命令.在每个界面中, "
        "都有一个支持每个Selenese命令的编程功能.客户端库接受Selenese命令,并将其传递给Selenium 服务器,以针对被测应用程序(AUT)处理特定操作或测试.客户端库还接收该命令的结果, "
        "并将其传递回您的程序.您的程序可以接收结果并将其存储到程序变量中,并将其报告为成功或失败,或者如果是意外错误,则可以采取纠正措施.因此, 要创建测试程序,只需编写一个使用客户端库API运"])
    def test_search_long_characters_exists(self, search_word):
        """
        测试步骤
        1. 打开ceshiren网站
        2. 点击首页的搜索按钮
        3. 点击高级搜索按钮
        4. 不输入搜索信息
        4. 点击搜索按钮
        6. 断言：搜索结果与实际结果一致。
        :return:
        """
        # 点击首页的搜索按钮
        self.driver.find_element(By.ID, "search-button").click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".searching").click()
        # 输入搜索信息：特殊字符
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys(search_word)
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        try:
            search_text = self.driver.find_element(By.CSS_SELECTOR, ".search-highlight").text
        except Exception:
            self.screenshot("search-long-characters-exists-fail")
            raise AssertionError(f"Search results are empty! Have created a new screenshot!")
        assert search_word in search_text, f"Search results are not empty!"

    # 异常场景：搜索内容为超长字符,该内容的帖子不存在
    @pytest.mark.parametrize("search_word", [
        "agsdiabdiuhadauidhauhsdiuahdiuahduihadhaidhaidhahduiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasdiasd"
        "以hbhgytfyuhjbhguyiuhojbvjgyiuhoijlnbhuhoijknlbhgiuhoijlknjbhuilknujbhvjygkjbhvjgujbjgygiuhjbhvjgygjbhvgfygiuhvjgfyguhvgfyuhvfugfu"])
    def test_search_long_characters_exists(self, search_word):
        """
        测试步骤
        1. 打开ceshiren网站
        2. 点击首页的搜索按钮
        3. 点击高级搜索按钮
        4. 不输入搜索信息
        4. 点击搜索按钮
        6. 断言：搜索结果不存在 提示:没有找到更多结果。
        :return:
        """
        # 点击首页的搜索按钮
        self.driver.find_element(By.ID, "search-button").click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".searching").click()
        # 输入搜索信息：特殊字符
        self.driver.find_element(By.CSS_SELECTOR, ".full-page-search").send_keys(search_word)
        # 点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        try:
            search_text = self.driver.find_element(By.CSS_SELECTOR, ".search-results h3").text
        except Exception:
            self.screenshot("search-special-characters-fail")
            raise AssertionError(f"Search results are empty! Have created a new screenshot!")
        assert "找不到结果。" == search_text, f"Search results are not empty!"
