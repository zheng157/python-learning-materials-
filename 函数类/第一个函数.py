name = "小郑"


def b1():
    """
    我喜欢编程
    """
    print("hello 1")
    print("hello 2")
    print("hello 3")

print("小郑")
b1()
print("小郑")
n = 2
def b2(x,y):
    global n
    return x * y * n
s = b2(10,2)
print(s)