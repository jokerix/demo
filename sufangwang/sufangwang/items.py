# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    rooms = scrapy.Field()
    area= scrapy.Field()
    address = scrapy.Field()
    district = scrapy.Field()
    sale = scrapy.Field()
    orinin_url = scrapy.Field()


class EsfhouseItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    floor = scrapy.Field()
    rooms = scrapy.Field()
    toward = scrapy.Field()
    address = scrapy.Field()
    year = scrapy.Field()
    area =scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    orinin_url = scrapy.Field()