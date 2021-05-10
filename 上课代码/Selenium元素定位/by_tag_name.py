# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度网站
driver.get("http://www.baidu.com")
# 通过tag_name定位元素
a = driver.find_elements_by_tag_name("a")
print(len(a))
for e in a:
    if e.get_attribute("name") == "tj_briicon":
        print(e.get_attribute("outerHTML"))
        print("--------------")
        # 打印元素文本
        print(e.text)