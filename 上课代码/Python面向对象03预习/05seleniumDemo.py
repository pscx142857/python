from time import sleep
from selenium import webdriver
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 进入百度页面
driver.get("http://www.baidu.com")
# 定位到输入框
kw = driver.find_element_by_id("kw")
# 在输入框中输入:python自动化测试
kw.send_keys("python自动化测试")
# 定位百度一下按钮
su = driver.find_element_by_id("su")
# 点击百度一下按钮
su.click()
# 等待2s
sleep(2)
# 获取页面标题,并且打印
title = driver.title
print(title)
# 检查python关键字是否在标题中
if "python" in title:
    print("python在标题中,成功!")
else:
    print("python不在标题中,失败")
# 关闭浏览器
driver.close()