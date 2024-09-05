
import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

reques = urllib.request.Request(url=url,headers=headers)


header = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(header)

response = opener.open(reques)


content = response.read().decode('utf-8')

print(content)