"""
单例模式:不管实例化多少次,始终得到的都是同一个对象
"""
class Singleton(object):
    # 类属性,存单例对象地址
    addr = None
    # 重写__new__方法,没有才创建,有就不用创建
    def __new__(cls, *args, **kwargs):
        if cls.addr == None:
            cls.addr = super().__new__(cls)
        return cls.addr
print(Singleton.addr)
s1 = Singleton()
print(Singleton.addr)
s2 = Singleton()
print(s1)
print(s2)