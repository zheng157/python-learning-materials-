import urllib.request
from lxml import etree
# http://www.bizhi360.com/meinv/index.html
# http://www.bizhi360.com/meinv/list_2.html
# /meinv/11671.html
def aa(i):

    if (i==1):
        url = 'http://www.bizhi360.com/meinv/index.html'
    else:
        url = 'http://www.bizhi360.com/meinv/list_'+str(i)+'.html'
    headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
    request = urllib.request.Request(url =url ,headers=headers)
    return request

def bb(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    a1 = etree.HTML(content)
    a2 = a1.xpath('//ul//a/@href')
    for i in a2:
        a3 = 'http://www.bizhi360.com'+i
        response=urllib.request.urlopen(a3)
        content = response.read().decode('utf-8')
        a4 =etree.HTML(content)
        url = a4.xpath('//figure//img/@src')[0]
        name = a4.xpath('//figure//img/@alt')[0]
        # url是相片，filename是名字
        urllib.request.urlretrieve(url=url, filename='./相片/' + name + '.jpg')




if __name__ == '__main__':
    a1 = int(input('请输入下载页码'))
    a2 = int(input('请输入结束页码'))
    for i in range(a1, a2 + 1):
        try:
            request = aa(i)
            bb(request)
        except urllib.error.URLError as e:
            print('下载第%d页时出现错误：%s' % (i, e))
            continue


