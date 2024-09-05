a1 = "hello python"
a2 = '我的名字是"小周"'

# print(a1[6:])
# for i in a2:
    # print(i)
# 统计长度
print(len(a2))

# 统计某一个小字符串出现的次数
print(a1.count("l"))
# 统计某一个小字符串出现的位置
print(a2.index("小"))
a3 ="2\u00b3"
print(a3)
#判断是否以指定字符串开始
#print(a1.startswith("hello"))
#判断是否以指定字符串开始
#print(a1.endswith("python"))
# print(a1.find("abd"))
#替换字符串
print(a2.replace("小周","小郑"))
