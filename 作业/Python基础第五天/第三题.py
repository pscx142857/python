#3.封装函数,实现返回三个数的最小值
def min_3(a,b,c):
    """
    返回三个数的最小值
    :param a: 第一个数字
    :param b: 第二个数字
    :param c: 第三个数字
    :return: 返回三个中最小的数字
    """
    ls = [a,b,c]
    mi = min(ls)
    return mi

print(min_3(101,2,99))