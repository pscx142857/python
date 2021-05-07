name = "模块中的变量"


def show():
    print("模块中的函数")


class Student(object):
    def info(self):
        print("模块中的类")

"""
__name__:
    在模块中运行 __name__ == "__main__"
    以导入的方式运行 __name__ == "模块名"
"""
# 测试的代码导入的时候不执行,在模块中执行
if __name__ == '__main__':
    print(name)
    show()
    s = Student()
    s.info()