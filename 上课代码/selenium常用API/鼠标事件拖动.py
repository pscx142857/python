"""
    drag_and_drop() 拖动
    move_to_element() 鼠标悬停在一个元素上
    click_and_hold() 按下鼠标左键在一个元素上
"""
# 引入ActionChains类
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# 导入webdriver
from selenium import webdriver

# 打开浏览器
driver = webdriver.Firefox()
# 打开练习网址
driver.get("file:///D:/%E5%90%8E/14_selenium%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2021_03_24_selenium%E9%A1%B5%E9%9D%A2%E8%87%AA%E5%8A%A8%E5%8C%96_day03/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/drop.html")

# 获取第一个元素
div1 = driver.find_element_by_id("div1")
div2 = driver.find_element_by_id("div2")
# 从div1拖动到div2
ActionChains(driver).drag_and_drop(div1,div2).perform()