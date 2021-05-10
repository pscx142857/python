# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开指定的网站
driver.get("https://www.baidu.com")
# 通过name定位元素find_element_by_name
wd = driver.find_element_by_name("wd")
# 打印定位元素所在行的代码
print(wd.get_attribute("outerHTML"))