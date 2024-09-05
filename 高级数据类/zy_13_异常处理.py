try:
    f = open('adc.txt','r')
    f.read()
except FileNotFoundError:
    print('异常')