"""
    is:是判断内存地址是否一样
    ==:是判断值是否一样
"""
name = "张三"
name1 = "张三"
# 因为字符串是不可变的,所以是简单数据类型,相同的数据不管定义多少次,都只会开辟一个内存空间
print(name is name1) # True
print(name == name1) # True

ls = ["张三","18"]
ls1 = ["张三","18"]
# list是可变的数据类型,复杂数据类型,相同的数据,定义几次就会开辟几次内存空间
print(ls is ls1)  # False
print(ls == ls1) # True