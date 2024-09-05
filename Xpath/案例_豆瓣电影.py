import json
import urllib.request
import urllib.parse
import csv



def a1(i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url_s = 'https://movie.douban.com/j/chart/top_list?'
    data = {
            'type':5,
            'interval_id':'100:90',
            'start':(i-1)*20,
            'limit':20
              }
    name = urllib.parse.urlencode(data)
    url_name = url_s + name
    request = urllib.request.Request(url=url_name, headers=headers)
    return request


def a2(url_name):
        response = urllib.request.urlopen(url_name)
        content = response.read().decode('utf-8')
        return content

def a3(content):

        wq = []
        content = json.loads(content)

        for i in content:
            title = i['title']
            cover_url = i['cover_url']
            regions =i['regions']
            regions = ', '.join(regions)
            types = i['types']
            types= ', '.join(types)
            rating= i['score']
            dat ={
                '名称':title,
                '相片':cover_url,
                '地址':regions,
                '剧情':types,
                '评分':rating
            }
            wq.append(dat)
        return wq
def a4(wq):
    with open('./案例_豆瓣电影/豆瓣电影.csv', 'a', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['名称', '相片', '地址', '剧情', '评分'])
        # 如果CSV文件为空，则先写入表头
        if f.tell() == 0:
            csv_writer.writeheader()
        # 写入所有电影数据
        csv_writer.writerows(wq)

    f.close()
if __name__ == '__main__':
    start_page = int(input('请输入下载起始页码: '))
    end_page = int(input('请输入下载结束页码: '))
    for page in range(start_page,end_page+1 ):
        url_name = a1(page)
        content= a2(url_name)
        wq = a3(content)
        a4(wq)
