# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https: // www.zhipin.com / c101010100 /?query = python & page = 1 ']

    rules = (
        # 匹配列表
        Rule(LinkExtractor(allow=r'.+?query=python&page=\d'), follow=True),
        # 匹配详情
        Rule(LinkExtractor(allow=r'.+job_detail/^[A-Za-z0-9]+$.html\d'), callback='parse_job', follow=False),

    )

    def parse_job(self, response):
        title = response.xpath("//h1[@class= 'name']/text()").get().strip()
        salary = response.xpath("//h1[@class = 'name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class= 'job_primary']/div[@class= 'info-primary']/p//text()").get().strip()
        city = job_info[0]
        work_year = job_info[1]
        education = job_info[2]
        item = BossItem(title=title, salary=salary, city=city, work_year=work_year, education=education)
        yield item
