import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def element_interaction():
    # 实例化driver对象
    driver=webdriver.Edge()
    driver.get("https://www.sogou.com/")
    # 定位到输入框进行输入操作
    driver.find_element(By.ID,"query").send_keys("霍格沃兹测试开发")
    time.sleep(2)
    # 清空输入框
    driver.find_element(By.ID,"query").clear()
    time.sleep(2)
    # 再次输入
    driver.find_element(By.ID,"query").send_keys("霍格沃兹测试开发2")
    # 点击搜索
    driver.find_element(By.ID,"stb").click()
    time.sleep(2)

def element_get_attr():
    driver = webdriver.Edge()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    web_element=driver.find_element(By.ID,"locate_id")
    # 不是每个元素都有文本信息
    print(web_element.text)
    # 获取元素的属性信息
    res = web_element.get_attribute("class")
    print(res)
if __name__ == '__main__':
    # element_interaction()
    element_get_attr()
