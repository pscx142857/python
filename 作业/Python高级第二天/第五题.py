# 5.写出下面代码的执行结果：
a = 'global'

def outer():
    def len(in_var):
        print('called my len() function: ', end="")
        l = 0
        for i in in_var:
            l += 2
        return l
    a = 'local'

    def inner():
        global len
        print(type(len))
        nonlocal a
        a += ' variable'  # 'local variable

    inner()
    print('a is', a)
    print(len(a)) #14

outer()
print(len(a))

print('a is', a)
