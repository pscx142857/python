"""
    私有成员:在类里面的是能被这个类使用的属性和方法,创建的对象也不能用
    私有: 只能自己用,别人都不能用
    成员: 属性和方法统称成员

    分类:
        私有属性:
            对象.__属性名 = 值
        私有方法:
            def __方法名():
"""
# 定义一个ATM类
class Atm:
    # 用初始化方法添加私有属性
    def __init__(self, money, key, pinmu):
        self.__money = money # 属性私有后不能被别人使用
        self.__key = key
        self.__pinmu = pinmu

    def get(self):
        money = input("请输入取钱的金额:")
        money = int(money)
        if money < 100 or money % 100 != 0:
            pass
        else:
            self.__countMoney(money) # 这个类可以使用私有方法
            self.__out(money)

    def __countMoney(self, money): # 方法私有后就不能被别人使用
        print(f"数{money}元")

    def __out(self, money):
        print(f"吐{money}元")


# 实例化一个Atm对象
atm = Atm(200, "英文键盘", "20寸")
# print(atm.__key) 不能使用私有属性
# print(atm.__out(500))  不能调用私有方法
atm.get()
