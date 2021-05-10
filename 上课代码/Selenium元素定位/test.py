name = "张三"

def show():
    print("外函数!")

    name = "李四"

    def inner():
        print("内涵式!")
        name = "王五"
        print(name)



    inner()
    print(name)

show()
print(name)