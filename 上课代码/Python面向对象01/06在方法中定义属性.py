class Student:
    # 有一个说话的方法
    def init(self,name,age=18,sex="男",tel=13456789123):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
        print(f"我的名字是{self.name},我的年龄是{self.age},我的性别是{self.sex},我的电话是{self.tel}")
    def speak(self):
        # self就是我自己,谁调用就是谁,self.name调用类里面的属性
        print(f"大家好,我是{self.name}")
        # 调用类里面的方法
        self.homework()

    def homework(self):
        print("我在写作业")
# 实例化对象
st1 = Student()
st2 = Student()

# 调用方法
st1.init("张三")
st2.init("李四",20)