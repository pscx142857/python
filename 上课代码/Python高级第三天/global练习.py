# 定义一个函数,在函数里面用global 引用len
print(len)
def info():
    global len

    def len():
        print("1")
    print(len)

info()
print(len)