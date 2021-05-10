"""
re模块:
    专门处理正则表达式的模块
        search():只匹配一次
        re.search("正则表达式","要匹配的字符串")

        findall():可以匹配多次
        re.findall("正则表达式","要匹配的字符串")
        返回的是一个列表
"""
# 导入re模块
import re
string = "kljal2skd3jlkfjs9al"

# 查询一次
res = re.search("ja",string)
print(res) # <re.Match object; span=(2, 4), match='ja'>
# 获取匹配到的对象上面的值
print(res.group()) # ja

# 匹配string中第一次出现任意数字的值
# res1 = re.search("[0-9]",string) #[0-9] 任意数字0到9
res1 = re.search("\d",string) #\d 任意数字0到9
print(res1.group())

string = """
    电话号码是: 028 1591347
    电话号码是: 028 3571486
    电话号码是: 028 1247583
    电话号码是: 028 1591574
    电话号码是: 028 0145721
"""
# 获取多次
ls = re.findall("\d+ \d+",string) # \d+:匹配0-9任意数字多次
print(ls) # ['028 1591347', '028 3571486', '028 1247583', '028 1591574', '028 0145721']