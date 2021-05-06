from selenium import webdriver
# 打开谷歌浏览器,模拟移动端
mobileEmulation = {"deviceName":"iPhone 6"}
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation",mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.baidu.com")