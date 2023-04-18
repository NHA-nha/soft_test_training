from selenium import webdriver

# 一定要在Edge后面加个括号，代表实例化这个类
driver = webdriver.Edge()
driver.get("https://ceshiren.com/")
print(driver.title)
driver.quit()
