from time import sleep
from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome()
# 打开百度网站
driver.get("http://www.baidu.com")
# 延迟两秒
sleep(2)
# 设置浏览器窗口大小
# driver.set_window_size(480,480)
# 浏览器窗口最大化
# driver.maximize_window()
# 延迟两秒
# 打开淘宝网站
driver.get("http://www.taobao.com")
# 后退
driver.back()
sleep(1)
# 前进
driver.forward()
sleep(1)
# 刷新
driver.refresh()
sleep(1)
# 关闭浏览器
driver.quit()