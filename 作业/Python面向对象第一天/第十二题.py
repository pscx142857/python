# 12.新建一个文件，定义一个计算类,有两个属性,数字1,数字2,具有 加 减 乘 除 方法
# 定义一个计算类
class Calculation:
    # 利用init方法设置两个属性,数字1和数字2
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    # 加法
    def add(self):
        return self.num1+self.num2
    # 减法
    def subtract(self):
        return self.num1-self.num2
    # 乘法
    def multiply(self):
        return self.num1*self.num2
    # 除法
    def divide(self):
        return self.num1 / self.num2
# 实例化一个计算类对象,传入两个数字
res = Calculation(10,5)
# 调用加法方法
print(res.add())
# 调用减法方法
print(res.subtract())
# 调用乘法方法
print(res.multiply())
# 调用除法方法
print(res.divide())