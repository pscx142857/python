# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度网站
driver.get("http://www.baidu.com")
# 通过link_text获取元素
e = driver.find_element_by_link_text("地图")
# 打印元素所在行的代码
print(e.get_attribute("outerHTML"))