# 讲目标网站的页面抓取下来


# 讲装取下来的数据根据一定规则提取


import requests
import lxml.html

etree = lxml.html.etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
response = requests.get(url, headers=headers)
text = response.text

html = etree.HTML(text)

ul = html.xpath("//ul[@class= 'lists']")[0]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li, encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    actors = li.xpath("@data-actors")[0]

    thumbaail = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'actors': actors,
        'thumbaail': thumbaail
    }
    movies.append(movie)
print(movies)