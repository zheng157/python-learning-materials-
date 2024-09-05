import urllib.request
import urllib.parse
import  json

def a1(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    data = {
    "cname": "南宁",
    "pageIndex": str(page),
    "pageSize": '10'
    }
    name = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url =url ,headers=headers,data=name)
    return request


def a2(request):
    requeste = urllib.request.urlopen(request)

    cont = requeste.read().decode('utf-8')

    return cont

def a3(page,cont):
    with open(f'./案例_肯德基/' + str(page) + '.json', 'w', encoding='utf-8') as f:
        f.write(cont)
    f.close()

if __name__ == '__main__':
    start_page = int(input('请输入下载起始页码: '))
    end_page = int(input('请输入下载结束页码: '))
    for page in range(start_page, end_page):
        request=a1(page)
        cont = a2(request)
        a3(page,cont)