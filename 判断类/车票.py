a1 = True
a2 = 40

if a1:
    print("车票检查通过，准备安检")
    "="*50
    if a2 >20:
        print("刀太长了，有 %d 公分长"%a2)
        print("不允许上车")

    else:
        print("安检过了，安全上车")
        print("安检过了，安全上车")




else:
    print("没有车票，请去买票")