"""
    拆包:
        拆包列表或者元组
            预先得到一个列表或者元组,如果元刚好要作为实参传递给函数使用,列表或者元组里面的元素拆包成位置参
"""
#求3个数的最大数
def max_3(a,b,c):
    """
    求3个数中的最大数
    :param a: 第一个数
    :param b: 第二个数
    :param c: 第三个数
    :return: 返回最大值
    """
    ls = [a,b,c]
    return max(ls)
ls = [12,88,44]
# ls列表里面的元素刚好要作为实参传递给max_3函数使用,那么就可以使用拆包
print(max_3(*ls))

tup = (5,6,4)
print(max_3(*tup)) # 元组也可以作为实参进行拆包, 格式:*列表或者*元组

# 返回三个数中的最小值
def min_3(a,b,c = 5):
    ls = [a,b,c]
    return min(ls)

ls = [99,4]

print(min_3(*ls)) # 这个元素个数,好像只要满足必传参数的个数就行了

"""
    拆包字典
        **字典
"""

dic = {"a":7,"b":88}
print(min_3(**dic)) # **dic,将这个字典拆包成关键字参数