# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度
driver.get("http://www.baidu.com")
# 超链接通过部分文本信息定位元素,by_partial_link_text
e = driver.find_element_by_partial_link_text("地")
# 打印元素所在行的代码
print(e.get_attribute("outerHTML"))