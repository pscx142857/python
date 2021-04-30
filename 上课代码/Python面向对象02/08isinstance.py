"""
    isinstance:判断是否是我们需要的类型
"""
num = "25"
if isinstance(num,int): # 判断是否是int类型
    print(num+10)
else:
    print(int(num)+5)