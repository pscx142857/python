"""
    异常的类型:
        推荐语法:
        try:
            可能出现异常的代码
        except Exception as e:
            对于异常的处理

    完整语法:
        try:
            可能出现异常的代码
        except Exception as e:
            对于异常的处理
        else:
            没有异常执行的代码
        finally:
            不管有没有异常,都会执行
"""
print("-----开始-------")
try:
    print(name) # NameError: name 'name' is not defined
    # open("data.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
except Exception as e:
    print("处理异常",e,type(e)) # 处理异常的代码
else:
    print("我的代码没有错误哦") # try里面没有异常,执行的代码
finally:
    print("-----结束-------") # 不管有没有异常,都会执行