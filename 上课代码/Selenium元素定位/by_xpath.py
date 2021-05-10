# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Firefox()
# 打开百度
driver.get("http://www.baidu.com")
# 通过xpath定位元素
kw = driver.find_element_by_xpath("//*[@id='kw']") # //*[@id="kw"]
re = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/div[3]/div/a[1]/div")
# 打印元素所在行的代码
print(kw.get_attribute("outerHTML"))
print(re.get_attribute("outerHTML"))
