"""
1.今天的上课代码实现一遍。
"""
"""
    私有成员:
        只有在类里面使用的方法和属性,
        __属性名
        __方法名
    对象也不可以使用
"""
# 创建一个学生类,含有私有属性和私有方法
class Stuedent(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def show(self):
        # 可以在类里面使用私有属性
        print(f"大家好我是{self.__name},我今年{self.__age}岁了")
        # 可以在类里面使用私有方法
        self.__eat()

    def __eat(self):
        print("我很会吃哦")
# 创建一个学生对象
s = Stuedent("张三",18)
# print(s.__name) 'Stuedent' object has no attribute '__name' 私有属性无法使用
# s.__eat() 'Stuedent' object has no attribute '__eat' 私有方法也无法使用
s.show()
"""
    __del__方法:
        在对象被销毁的时候执行
        在Python语言中,一般不用我们手动销毁对象,python.exe解释器会自动帮助我们销毁
        Python代码执行完的时候对象就被销毁
        当对象的引用计数为零的时候被销毁
"""
# 定义一个教师类
class Teacher(object):
    def __init__(self):
        print("我在创建对象的时候被执行")
    def __del__(self):
        print("我在对象销毁的时候被执行")

# 实例化一个教师对象
t = Teacher()
t2 = t
del t # 对象的引用计数为零的时候,对象会被销毁,这里有两个引用计数,只减掉了一个,引用计数不为零,所以不会在这里销毁
print("这是一条华丽的分割线----------------") # 代码执行完毕,对象会被自动销毁

"""
    继承:
        发生在两个类之间,子类可以继承父类的所有成员,属性和方法
        私有成员不可以被继承
        子类也可以拥有自己的属性和方法
        所有的类都会默认继承object
        dir(对象),可以查看对象中的成员 
"""
# 定义一个父类
class Father(object):
    def speak(self):
        print("我会说话哦")
# 定义一个儿子类,继承父类
class Son(Father):
    pass

# 实例化一个儿子对象
s = Son()
# 儿子继承了父类,就拥有了父类的方法,就可以调用了
s.speak()

"""
    继承的分类
    1,单继承
        一个父类,一个子类
    2,继承链
        a继承b,b继承c,c继承d,a就会拥有b,c,d的属性和方法
    3,多继承
        一个类可以继承多个父类
"""
# 定义一个动物类
class Animal(object):
    def run(self):
        print("所有的动物都会跑")
# 定义一个狗类
class Dog(Animal):
    def eat(self):
        print("我爱吃骨头")
# 定义一个傻子类
class Shazi(object):
    def show(self):
        print("我是傻子")
# 定义一个哈士奇类
class Husky(Dog,Shazi):
    def fadai(self):
        print("一边吃骨头一边发呆")

# 实例化一个哈士奇对象
h = Husky()
# h继承了狗类和傻子类,调用者两个类的方法
h.show()
h.eat()
# h继承了狗类,狗类继承了动物类,可以调用动物类的方法
h.run()
"""
    重写:
        子类的属性名和方法名和父类的一样时,就会重写父类的方法和属性,以子类为准
"""
# 定义一个A类
class A(object):
    def say(self):
        print("hi")
# 定义一个B类继承A类,重写say方法
class B(A):
    def say(self):
        print("我被重写了")

#实例化一个B类,调用属性和方法来验证
b = B()
b.say() # say方法被重写后以子类的为准
"""
    __init__方法的重写问题:
    super().父类的方法名() ,在子类中调用父类的方法执行一次
"""
# 定义一个C类
class C(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
# 定义一个D类
class D(C):
    def __init__(self,name,age,sex):
        # 调用一次父类的init方法,子类就有父类的属性了
        super().__init__(name,age)
        self.sex = sex
    def show(self):
        print(f"我的名字是{self.name},我的年龄是{self.age},我是{self.sex}的")

d = D("张三",18,"女")
d.show()
"""
    多态:
    在python中,所有的子类都可以重写父类的方法,
    这个时候虽然子类和父类都拥有相同的方法名,但实现的效果是不同的,这就是多态
"""
# 定义一个E类,有eat的方法
class E(object):
    def eat(self):
        print("我是E的吃")
# 定义一个F类,继承E类,重写eat方法
class F(E):
    def eat(self):
        print("我是F的吃")
# 定义一个G类,继承F类,重写eat方法
class G(F):
    def eat(self):
        print("我是G的吃")
# 实例化对象
e = E()
e.eat()
e = F()
e.eat()
e = G()
e.eat()  # 相同的方法名,不同的效果,多态
"""
    isinstance:可以判断是否是我们需要的类型
"""
st = "123456"
print(isinstance(st, str)) # True , st是一个字符串的类型