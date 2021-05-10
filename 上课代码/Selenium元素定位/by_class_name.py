# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度网站
driver.get("https://www.baidu.com")
# 通过class_name定位元素
s_ipt = driver.find_element_by_class_name("s_ipt")
# 打印定位元素所在行的代码
print(s_ipt.get_attribute("outerHTML"))