"""
13.定义一个高级字符串工具类
    具有如下方法:
        1)将给定字符串反转（传入abcd返回dcba）
"""
# 定义一个高级字符串类
class Adstr:
    # 定义个反转方法,可以将传入的字符串反转
    def rever(self,st):
        """
        字符串反转
        :param st: 字符串
        :return: 返回反转后的字符串
        """
        # 利用切片,使这个字符串反转
        return st[::-1]
# 实例化一个高级字符串类
ads = Adstr()
# 调用方法
st = ads.rever("abcde")
# 打印
print(st)
"""
    方法二:reverse
"""
# 定义一个高级字符串类
class Adstr_2:
    # 定义个反转方法,可以将传入的字符串反转
    def rever(self,st):
        """
        字符串反转
        :param st: 字符串
        :return: 返回反转后的字符串
        """
        # 利用reverse,使这个字符串反转
        ls = list(st)
        ls.reverse()
        return "".join(ls)
# 实例化一个高级字符串类
adstr_2 = Adstr_2()
# 调用方法
st_2 = adstr_2.rever("abcd")
# 打印
print(st_2)