# -*- coding: utf-8 -*-
import scrapy
from qsbk.qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        duanzidiv = response.xpath("//div[@id = 'content-left']/div")
        for duanzi in duanzidiv:
            author = duanzi.xpath(".//h2/text()").get().strip()
            content = duanzi.xpath(".//div[@class= 'content']//text()").getall()
            content = ''.join(content)
            item = QsbkItem(author=author, content=content)
            yield item
