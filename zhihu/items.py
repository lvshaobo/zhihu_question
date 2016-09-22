# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()          # Web Title
    name = scrapy.Field()           # Job Title
    corp = scrapy.Field()           # Company Name
    addr = scrapy.Field()           # Address
    salary = scrapy.Field()         # Salary
    popu = scrapy.Field()           # Recruiting Numbers
    question = scrapy.Field()       # Question Link
