from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 首先实例化driver对象，Edge()一定要加括号
    driver = webdriver.Edge()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 1.ID定位，第一个参数传达定位方式，第二个参数传递定位元素，调用这个方法的返回值为webElement
    # web_element = driver.find_element(By.ID,"locate_id")
    # 2.Name定位
    # 没报错就证明元素找到了，报错no such element，代表元素定位可能出错
    # driver.find_element(By.NAME,"locate")
    # 3.Css选择器定位
    # driver.find_element(By.CSS_SELECTOR,"#locate_id")
    # 4.xpath表达式定位
    # driver.find_element(By.XPATH,'//*[@id="locate_id"]')
    # 5.通过链接文本的方式 (1)元素一定是a标签  (2)输入的元素为标签内的文本
    driver.find_element(By.LINK_TEXT,"元素定位")

if __name__=='__main__':
    web_locate()
