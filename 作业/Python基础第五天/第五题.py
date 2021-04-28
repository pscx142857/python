#5.设计根据QQ和密码登录的过程(QQ和密码预设为指定的值). 执行结果为登录是否成功(boolean类型的值)
def login():
    """
    验证账号密码是否正确,正确时提示登录成功,错误时提示登录失败
    :return:
    """
    username = input("请输入你的账号:")
    password = input("请输入你的密码:")

    if username == "123456" and password == "654321":
        print("恭喜你登录成功")
    else:
        print("对不起,登录失败")

login()