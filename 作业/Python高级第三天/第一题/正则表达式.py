"""
正则表达式:
    专门匹配字符串的
    Python中有专门处理正则的模块re
"""
# 导入re模块
import re
# 定义一个字符串
string = "addadd123阿萨德发1的36三adda大师傅"
# search只查找一次,匹配字符串中的第一个数字
res = re.search("\d",string).group()
print(res)
# 匹配第一次出现的数字,不限个数
res = re.search("\d+",string).group()
print(res)
# 匹配a开头a结尾的字符串,默认是贪婪模式
res = re.search("a.+a",string).group()
print(res) # addadd123阿萨德发的三adda
# 修改成非贪婪模式
res = re.search("a.+?a",string).group()
print(res) # adda
# findall 查找不止一次,返回的是一个列表
ls = re.findall("\d+",string)
print(ls) # ['123', '1', '36']