"""
    匿名函数:
        lambda [形参1,形参2,...] : 函数体

        特点:
            1,一行写完(比较简单的功能),不需要写return自动返回函数计算结果
            2,匿名函数会作为参数传递给普通函数使用

"""
sum = lambda a,b : a + b
print(sum(1,2))

def cc(a,b,op):
    return op(a,b)

i = cc(5,7,lambda x,y:x+y)
print(i)