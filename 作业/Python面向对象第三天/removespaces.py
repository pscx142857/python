"""
可以去除传入的字符串里面的所有空格,返回去除空格之后的字符串
"""
def stripspace(st):
    """
    去除字符串中所有的空格
    :param st: 传入的字符串
    :return: 返回去除空格后的字符串
    """
    return st.replace(" ","")