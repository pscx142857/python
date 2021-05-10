"""
    正则表达式默认的是贪婪模式
"""
string = "abdcda abcd lkjadsladdddd"
# 导入re模块
import re
res = re.search("a.*a",string).group() # abdcda abcd lkjadsla
print(res)
# 加个问号,就改成非贪婪模式
res = re.search("a.*?a",string).group() # abdcda
print(res)