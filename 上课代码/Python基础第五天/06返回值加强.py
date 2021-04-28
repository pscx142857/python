#return 可以不写,如果不写就是返回None
def show():
    name = 1
print(show()) # None
#return一旦执行,那么函数就会终止
def show():
    print("111111")
    return 1
    print("2222") # rerun一旦执行,那么函数终止,这条代码不再执行
show()
#一个函数里面可以写多个return
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(5,9))
#return可以返回多个值,得到一个元组
def show():
    return 1,2,3,4
st = show()
print(st)  # (1, 2, 3, 4) 得到一个元组