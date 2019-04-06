# -*- coding: utf-8 -*-
import scrapy
import re
from sufangwang.items import NewhouseItem, EsfhouseItem


class SoufangSpider(scrapy.Spider):
    name = 'soufang'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class = 'outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            if province == "其它":
                continue
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()

                url_model = city_url.split("//")
                scheme = url_model[0]
                domain = url_model[1]
                juti = domain.split(".")
                cssx = juti[0]
                fang = juti[1]
                u = juti[2]
                # 构建新房
                if 'bj.' in domain:
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    esfhouse_url = 'https://esf.fang.com/'
                else:
                    newhouse_url = scheme + '//' + cssx + '.newhouse.' + fang + "." + u + "/house/s/"
                    # 构建二手房
                    esfhouse_url = scheme + '//' + cssx + '.esfhouse.' + fang + "." + u + "/house/s/"

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={'info': (province, city)})
                yield scrapy.Request(url=esfhouse_url, callback=self.parse_esfhouse, meta={'info': (province, city)})

    def parse_newhouse(self, response):

        province, city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class = 'nlcd_name']/a/text()").get().split()
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x: re.sub(r'\s', '', x), house_type_list))
            rooms = list(filter(lambda x: x.endswith("居"), house_type_list))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r"\s|-|/", "", area)
            address = li.xpath(".//div[@class = 'address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class= 'address']/a//text()").getall())
            district = re.search(r".*\[(.+)\].*", district_text).group(1)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class= 'nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            origin_url = li.xpath(",//div[@class = 'nlcd_name']/a/@href").get()

            item = NewhouseItem(name=name, rooms=rooms, area=area, address=address, district=district, sale=sale,
                                price=price, origin_url=origin_url, city=city, province=province)
            yield item

        next_url = response.xpath("//div[@class= 'page']//a[@class = 'next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={'info': (province, city)})

    def parse_esfhouse(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[@class= 'houseList']/dl")
        for dl in dls:
            item = EsfhouseItem(province=province, city=city)
            item['name'] = dl.xpath(".//p[@class= 'mt10']/a/span/text()").get()
            infos = dl.xpath(".//p[@class= 'mt12;]/text()").getall()
            infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
            for info in infos:
                if '厅' in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                else:
                    item['year'] = info.replace('建筑年代: ', "")
            address = dl.xpath(".//p[@class = 'mt10']/span/@title").get()
            item['address'] = address
            item['area'] = dl.xpath(".//div[contains(@class,'area')]/p/text()").get()
            item['price'] = "".join(dl.xpath(".//div[@class= 'moreInfo']/p[1]//text()").getall())
            item['unit'] = "".join(dl.xpath(".//div[@class= 'moreInfo']/p[2]//text()").getall())
            detail_url = dl.xpath(".//p[@class = 'title']/a/@href").get()
            item['origin_url'] = response.urljoin(detail_url)
            yield item
        next_url = response.xpath("//a[@id = 'PageControll_hlk_next']/@href").get()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esfhouse,
                             meta={'info': (province, city)})
