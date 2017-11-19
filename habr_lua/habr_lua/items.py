# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HabrLuaItem(scrapy.Item):
    author = scrapy.Field()
    date = scrapy.Field()
    hubs = scrapy.Field()
    type_label = scrapy.Field()
    text = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()
    rating = scrapy.Field()
    bookmarks = scrapy.Field()
    views = scrapy.Field()
    comments_count = scrapy.Field()
