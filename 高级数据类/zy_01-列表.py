a1 = ["zheng","yi","udb","anb"]


a2 = {}  # 创建一个空字典

for i in range(0, len(a1), 2):
    key = a1[i]  # 列表元素作为键
    value = a1[i+1]  # 下一个列表元素作为值
    a2[key] = value  # 将键值对添加到字典中

print(a2)

a1[0] = "郑艺"
 #append末尾增加一个数据
a1.append("anb")
 #insert 指只一个地方增加一个数据
a1.insert(1,"小郑")

a2 = ["小孙","小铃","小天"]
 # extend 两个列表合起来
a1.extend(a2)
 #remove 删除指定的数据
a1.remove("小铃")
 # pop 删除末尾的一个数据
a1.pop()
 #clear清空数据
# a1.clear()

a3 = input('请输入你想知道的名字')
# if a3 in a2:
#     print('在')
# else:
#     print('不在')

if a3 not in a2:
    print('在')
else:
    print('不在')

