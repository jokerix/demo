import lxml.html

etree = lxml.html.etree
import requests

Base_DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",

}


def get_detail_urls(url):
    # url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"

    response = requests.get(url, headers=HEADERS)
    # text = response.content.decode('gbk')
    text = response.text
    html = etree.HTML(text)

    detail_urls = html.xpath("//table[@class='tbspan']//a//@href")
    # for detail_url in detail_urls:
    #     print(Base_DOMAIN + detail_url)

    detail_urls = map(lambda url: Base_DOMAIN + url, detail_urls)
    return detail_urls


def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            break
        break


def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class= 'title_all']//font[@color= '#07519a']/text()")[0]
    # for x in title:
    #     print(etree.tostring(x, encoding='utf-8').decode('utf-8'))
    print(title)
    movie['title'] = title

    zoomE = html.xpath("//div[@id = 'Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    haibao = imgs[1]
    movie['cover'] = cover

    # 第二种
    # zoomE = html.xpath("//div[@id= 'Zoom']//img/@src")
    # cover = zoomE[0]
    # print(cover)

    # 处理数据的函数
    def parse_info(info, rule):
        return info.replace(rule, '').strip()

    infos = zoomE.xpath(".//text()")
    for info in infos:
        if info.startswith("◎年　　代 "):
            info = parse_info(info, "◎年　　代 ")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地 ")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别 ")
            movie['leibei'] = info


if __name__ == '__main__':
    spider()
