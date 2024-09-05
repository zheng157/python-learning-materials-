def b1(c1,c2):

    print(c1 * c2)


def b2(c1,c2):
    """打印多行分隔钱

    :param c1:分隔钱使用的分隔字符
    :param c2:分隔钱重复的次数
    """
    a1 = 0
    while  a1 <= 5 :

        b1(c1,c2)

        a1 += 1
b1("+",50)