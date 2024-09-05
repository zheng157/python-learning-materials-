a1 = {"mane":"小艺","mane2":"小郑"}
# 取值
print(a1["mane"])
# 增加
a1["age"] = "18"
# 修改
a1["mane"] = "小小艺"

# 删除
a1.pop("mane")
print(a1)


a2 = {"mane3":"小萍","age1":19}
# 统计健值对数量
print(len(a2))
# 合并字典
a1.update(a2)

# 清空字典
a2.clear()
print(a2)