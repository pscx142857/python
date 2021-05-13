"""
在ActionChains类中提供了鼠标事件的方法
    context_click() 右击
    double_click()  双击
"""
# 引入ActionChains类
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
# 导入webdriver
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度
driver.get("http://www.baidu.com")

# 通过css选择器定位设置按钮
sz = driver.find_element_by_css_selector("#s-usersetting-top")
# 鼠标悬停
ActionChains(driver).move_to_element(sz).perform()