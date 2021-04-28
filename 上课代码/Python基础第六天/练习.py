# 1.程序启动，提示用户登录或者注册
# 2.选择注册->要求输入用户名和密码->返回注册提示信息
# 3.选择登录->要求输入用户和密码->判断是否登录成功

# 注册
info = [
    {"username":"丫丫","password":"123456"},
    {"username":"兮兮","password":"654321"}
]
def register():
    username = input("请输入用户名:")
    password = input("请输入密码:")

    user = {"username":username,"password":password}
    info.append(user)
    print("恭喜你注册成功")
    print("您的账号是:",username)
    print("您的密码是:",password)

# 登录
def login():
    username = input("请输入用户名:")
    password = input("请输入密码:")

    for i in info:
        if i["username"] == username and i["password"] == password:
            print("恭喜你登录成功")
            break
    else:
        print("对不起,登录失败")
while True:
    st = input("请选择需要的功能(1-注册 2-登录 3-退出):")
    if st == "1":
        register()
    elif st == "2":
        login()
    elif st == "3":
        exit("退出系统")
    else:
        print("对不起输入错误,请重新输入")
