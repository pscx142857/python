# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开指定的网站
driver.get("https://www.baidu.com")
# 通过id定位元素find_element_by_id
kw = driver.find_element_by_id("kw")
# 打印定位元素所在行的代码
print(kw.get_attribute("outerHTML"))
# print(kw.text)
