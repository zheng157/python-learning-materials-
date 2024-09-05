def b1():

    a1 = 1
    while a1 <= 9:

        a2 = 1
        while a2 <= a1:
            #print("*" ,end="")
            print("%d * %d = %d" % (a2, a1,a2*a1), end="\t")
            a2 += 1

        print("")
        a1 += 1