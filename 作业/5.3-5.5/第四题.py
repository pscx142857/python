"""
4. 使用列表推导对列表中的每个奇数取平方。 该列表由逗号分隔的数字序列输入。
	输入 : 1,2,3,4,5,6,7,8,9
	输出 : 1,9,25,49,81
"""
def oddsquare(ls):
    """
    计算列表中奇数的平方
    :param ls: 元素是int类型的列表
    :return:
    """
    # 定义一个空列表
    ls_new = list()
    # 遍历传入的列表,提取出奇数,然后取平方,追加到空列表中
    for i in ls:
        if i % 2 != 0:
            ls_new.append(i*i)
    print(ls_new)
# 定义一个列表
ls = [1,2,3,4,5,6,7,8,9]
# 调用函数
oddsquare(ls)