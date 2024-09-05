import urllib.request
import urllib.parse
import requests
import json



# url= 'https://fanyi.baidu.com/sug'
#
# header ={
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
# }
# data = {
# 'kw':'spider',
#
# }
# data = urllib.parse.urlencode(data).encode('utf-8')
#
# request = urllib.request.Request(url=url,headers=header,data=data)
#
# requeste = urllib.request.urlopen(request)
#
# content = requeste.read().decode('utf-8')
#
# conten = json.loads(content)
# print(conten)


url= 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

header ={
    'Cookie':'__yjs_duid=1_e44afcd7bebf02468420a81935f971ba1640684837108; BIDUPSID=8E56D898A09AD2EC56AA353CBF97B61A; BAIDUID=8E56D898A09AD2EC5CB22121719D90D1:FG=1; PSTM=1680682627; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=8E56D898A09AD2EC5CB22121719D90D1:FG=1; ZFY=lfLtdZKbnvijNE7cwm2T:BTX4QYb5mRY6lGQ:AHDcLbP8:C; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=aa82876c-bbff-4b9e-9df0-62c7d38bcb80&ss=lkcm50xp&sl=b&tt=1kgp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=37t4&ul=3ucr&hd=3udb"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1687517288,1689963211,1690035939; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1690036877; ab_sr=1.0.1_MTI1YzE5N2Y0YTllNmJmMzU3OTkyNzYwYmQyNjI3ZDY0ZTliMjEwZDhiNDVmZTY3NzcyOWJkZGJjNjI4YzJhY2MzMGIwYmY0ZTJmMzYwYTI0NzRlMDdkNDdhNWVhMWNmOWZjNzE4NTdjMGNkNTRiYTc3ODNiMTQyMWJkZjVlOGMzNTBmYzcwNDA1YzkyNzg1MWFlYjJkMzA1MmM4NmNmMg=='
}
data = {
'rom': 'en',
'to': 'zh',
'query': 'spider',
'transtype': 'realtime',
'simple_means_flag': '3',
'sign': '63766.268839',
'token': '11e526ca8c03cdc6f0e7699363578775',
'domain': 'common',
'ts': '1690036885059'
}
data = urllib.parse.urlencode(data).encode('utf-8')

# print(data)
request = urllib.request.Request(url=url,headers=header,data=data)

requeste = urllib.request.urlopen(request)

content = requeste.read().decode('utf-8')

conten = json.loads(content)
print(conten)