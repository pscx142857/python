"""
    单例模式:
        只需要这个类创建一个实例就行了,没必要创建多个对象
        通过重写__new__方法来实现
        只有当没有创建过对象的时候才创建,
        如果已经创建了就直接返回创建过的对象
        用私有属性保存好这个对象,保护不被修改
"""
class Singleton(object):
    # 私有属性保存对象
    __instance = None
    # 自定义创建对象,重写__new__方法
    def __new__(cls,name):
        # 判断是否已经创建,没有才创建
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,name):
        self.name = name
# 实例化一个对象
s = Singleton("第一")
print(id(s))
s2 = Singleton("第二")
print(id(s2))

x = 1
