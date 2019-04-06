import requests
import os
import re
from urllib import request
import lxml.html

etree = lxml.etree


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class != 'gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，,。！!,]', '', alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        print(filename)
        print(1 + 1)

        request.urlretrieve(img_url, 'images/' + filename)
        # print(img_url)


def main():
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)
        break


if __name__ == '__main__':
    main()
