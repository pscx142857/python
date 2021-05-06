"""
单例模式:不管实例化多少次,始终得到的都是同一个对象
"""
class Singleton(object):
    # 类属性,存单例对象地址

    # 重写__new__方法,没有才创建,有就不用创建
    def __new__(cls, *args, **kwargs):
        addr = None
        if addr == None:
            addr = super().__new__(cls)
        return addr
s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)