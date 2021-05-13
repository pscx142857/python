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

# 用link_text获取新闻链接元素
li = driver.find_element_by_link_text("新闻")
# 执行鼠标右击的操作
ActionChains(driver).context_click(li).perform()
sleep(1)
# 用xpath获取换一换元素
el = driver.find_element_by_xpath("//*[@id='hotsearch-refresh-btn']/span")
# 执行鼠标双击的操作
ActionChains(driver).double_click(el).perform()