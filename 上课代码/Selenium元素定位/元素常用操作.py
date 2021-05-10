# 导入webdriver模块
from time import sleep

from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度
driver.get("http://www.baidu.com")
# 通过xpath获取搜索框
kw = driver.find_element_by_xpath("//*[@id='kw']")

# 模拟输入
kw.send_keys("源码时代")
sleep(1) # 延迟两秒
# 清空文本
# kw.clear()
# 通过css获取百度一下按钮
su = driver.find_element_by_css_selector("#su")
# 点击百度一下按钮
su.click()
# 获取第二条数据
s2 = driver.find_element_by_xpath("//*[@id='1']/h3/a[1]")
s2.click()

# 1. size                 返回元素大小
print(s2.size)
# 2. text                 获取元素的文本
print(s2.text)
# 3. title                 获取页面title
print(driver.title)
# 4. current_url            获取当前页面URL
print(driver.current_url)
# 5. get_attribute("xxx") 获取属性值;xxx：要获取的属性
print(s2.get_attribute("data-click"))
# 6. is_display()            判断元素是否可见
print(s2.is_displayed())
# 7. is_enabled()            判断元素是否可用
print(s2.is_enabled())