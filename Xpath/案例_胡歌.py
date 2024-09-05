# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%83%A1%E6%AD%8C'
import urllib.request
import urllib.parse



url= 'https://www.baidu.com/s?'


header ={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}
data = {
    'wd':'胡歌',
    'sex':'男'
}

name = urllib.parse.urlencode(data)


request = urllib.request.Request(url= url+name,headers=header,method=None)

reques = urllib.request.urlopen(request).read().decode('utf-8')

print(reques)