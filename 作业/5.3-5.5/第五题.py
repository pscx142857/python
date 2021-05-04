"""
5. 网站要求用户输入用户名和密码进行注册。 编写程序以检查用户输入的密码是否有效。
	以下是检查密码的标准：
		-[a-z]之间至少1个字母
		-介于[0-9]之间的至少1个数字
		-[A-Z]之间至少1个字母
		-[$＃@]中的至少1个字符
		-交易密码的最小长度：6
		-交易密码的最大长度：12
	您的程序接受输入的密码, 根据以上的条件 判断密码是否满足要求。
"""
# 定义一个变量作标识,True:注册成功,False:注册失败
flag = True
# 所有的小写字母
low_st = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# 所有的大写字母
up_st =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 0-9的数字
digit = ["0","1","2","3","4","5","6","7","8","9"]
# 3个特殊字符
st = ["$","#","@"]
username = input("请输入用户名:")
password = input("请输入密码:")
# 长度小于6,注册失败
if len(password) < 6:
    flag = False
# 长度大于12,注册失败
elif len(password) > 12:
    flag = False
for i in password:
    # 必须至少一个是小写字母
    if i in low_st:
        break
else:
    flag = False

for i in password:
    # 必须至少一个是大写字母
    if i in up_st:
        break
else:
    flag = False

for i in password:
    # 必须至少一个是那3个特殊字符
    if i in st:
        break
else:
    flag = False

for i in password:
    # 必须至少一个是0-9的数字
    if i in digit:
        break
else:
    flag = False
if flag:
    print("恭喜你注册成功")
else:
    print("对不起,你输入的密码不满足要求")
