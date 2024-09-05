import  urllib.request

'''url_page = 'https://www.baidu.com/'''

#.urlretrieve第一个参数是下载的路径，第二个参数是文件名

'''urllib.request.urlretrieve(url_page,'baidu.html')'''


#下载图片
'''url_img = 'https://www.gov.cn/images/gtrs_logo_lt.png'

urllib.request.urlretrieve(url_img,'图片.png')'''

# 下载视频

'''url_mp4 = 'https://vd3.bdstatic.com/mda-pgj8hidvn9m5hh3f/720p/h264/1689832848128070931/mda-pgj8hidvn9m5hh3f.mp4?v_from_s=hkapp-haokan-hnb&auth_key=1689956799-0-0-e5b1496b21c28864fc6087c652eac3e0&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=1599418511&vid=7797301258883681434&abtest=111611_6&klogid=1599418511'


urllib.request.urlretrieve(url_mp4,'视频.mp4')'''


url = 'https://www.baidu.com/'
header ={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}

request = urllib.request.Request(url,headers=header,method=None)

reques = urllib.request.urlopen(request).read().decode('utf-8')

print(reques)

