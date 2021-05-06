"""
手动抛出异常:
    语法: raise 异常的类名("异常的描述信息")
"""
username = input("请输入用户名:")
password = input("请输入用户名:")
if username == "admin" and password == "123456":
    print("登录成功")
else:
    print("登录失败")
    raise Exception("登录失败了") # 手动抛出异常
print("购物")