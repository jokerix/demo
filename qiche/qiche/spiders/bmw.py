# -*- coding: utf-8 -*-
import scrapy

from qiche.items import QicheItem


class BmwSpider(scrapy.Spider):
    name = 'bmw'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series-s38004/511.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class ='uibox']")
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class= 'uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            urls = list(map(lambda url: response.urljoin(url), urls))
            print(urls)
            item = QicheItem(category=category, image_urls=urls)
            yield item
