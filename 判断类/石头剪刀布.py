import random

a1 = int(input("请输入你要出的 石头(1) 剪刀(2) 布(3)："))
a2 = random.randint(1,3)

print("我出 %d PK 电脑出%d" % (a1,a2))


if ((a1 == 1 and a2 ==2)
        or (a1 == 2 and a2 ==3)
        or (a1 == 5 and a2 ==1)):
    print("我赢了")
elif a1 == a2:
    print("平局")
else:
    print("电脑赢了")