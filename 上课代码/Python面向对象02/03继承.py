"""
    继承:发生在两个类之间,有一个父类,一个子类,子类继承了父类就有了父类所有的属性和方法
        继承之后这些属性和方法就是子类的了
        子类可以拥有自己的方法和属性
        不写继承,所有的类默认继承 object
        私有成员不能被继承
    dir(对象):可以查对象中所有的成员

"""
class Father(object):

    def ft(self):
        print("我会敲代码,想学吗")

class Son(Father): # 继承父类,就有了父类的方法
    def fb(self):
        print("我还会搞测试")
# 实例化对象
s = Son()
print(dir(s))
s.ft()
s.fb()