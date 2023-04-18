import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def web_wait():
    driver = webdriver.Edge()
    driver.get('https://vip.ceshiren.com/')
    # 不加等待，可能因为网速等原因产生报错
    # ******强制等待
    # ===报错：no such element ：unable to locate element
    # ===原因：页面未加载完成，就去查找该元素，此时这个元素还未加载出来
    # ===解决方案：在no such element ：unable to locate element报错之前加强制等待，等待页面渲染完成
    # time.sleep(3)
    # ******隐式等待
    # 强制等待问题：不确定页面的加载时间，可能会因为等待时间过长而影响用例执行
    # 使用方法：在代码一开始运行的时候就添加隐式等待的配置，注意，隐式等待是全局生效，所以在所有的find_element动作之前就执行此代码
    # 注意：隐式等待只能解决元素查找问题，而不能解决元素交互的问题
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,"//*[text()='个人中心']")

def wait_show():
    driver = webdriver.Edge()
    driver.get('https://vip.ceshiren.com/#/ui_study')
    # 问题：元素可以找到，但是点击效果没有触发
    # 第一个参数是driver，第二个参数是最长等待时间，until方法内需要结合expected_conditions或者自己封装的方法进行使用
    # expected_conditions的参数传入的都是一个元组
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"success_btn")))
    driver.find_element(By.CSS_SELECTOR,"#success_btn").click()
if __name__=='__main__':
    # web_wait()
    wait_show()
