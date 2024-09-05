
# #将python对象变成json字符串
# fp = open('test.txt','w',encoding='utf-8')
#
# name_list = ['zs','ls']

import json

# names = json.dumps(name_list)
#
# fp.write(names)
# fp.close()
# print(names)

# names = json.dump(name_list,fp)



#将json字符串变成python对象
fp = open('test.txt','r')

# content = fp.read()
#
# print(content)
# print(type(content))
#
# resilt = json.loads(content)
#
# print(resilt)
# print(type(resilt))

a1 = json.load(fp)
print(a1)

fp.close()
