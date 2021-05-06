from time import sleep
from selenium import webdriver
# 隐藏浏览器
options = webdriver.ChromeOptions()
options.add_argument("-headless")
# 打开浏览器
driver = webdriver.Chrome(options = options)
# 打开网站
driver.get("http://www.baidu.com")
# 获取标题
title = driver.title
print(title)
# 关闭浏览器
driver.quit()