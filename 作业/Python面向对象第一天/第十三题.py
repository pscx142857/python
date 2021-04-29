"""
13.定义一个高级字符串工具类
    具有如下方法:
        1)将给定字符串反转（传入abcd返回dcba）
"""
# 定义一个高级字符串类
class Adstr:
    # 定义个反转方法,可以将传入的字符串反转
    def rever(self,str):
        """
        字符串反转
        :param str: 字符串
        :return: 返回反转后的字符串
        """
        # 利用切片,使这个字符串反转
        return str[::-1]
# 实例化一个高级字符串类
ads = Adstr()
# 调用方法
str = ads.rever("abcde")
# 打印
print(str)
