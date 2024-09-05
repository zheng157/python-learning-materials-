import urllib.request
# 获取网页的源码
# 解析解析的服务器响应的文件etree.HTML
# 打印

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
# 请求对象的定制
request = urllib.request.Request(url =url ,headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

from lxml import etree
# 解析服务器响应的文件
a1 = etree.HTML(content)



a2 = a1.xpath('//input[@id="su"]/@value')[0]
print(a2)