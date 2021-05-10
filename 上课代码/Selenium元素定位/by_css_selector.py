# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开网址
driver.get("http://www.baidu.com")
# 通过css选择器定位元素
kw = driver.find_element_by_css_selector("li.hotsearch-item:nth-child(5) > a:nth-child(1) > span:nth-child(2)")
# 打印元素所在行的代码
print(kw.get_attribute("outerHTML"))