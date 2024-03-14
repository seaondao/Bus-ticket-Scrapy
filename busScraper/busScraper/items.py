# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BusscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def changeName(value):
    if "名鉄" in str(value):
        return "名古屋駅"
    elif "金沢" in str(value):
        return "金沢駅"
    elif "高山" in str(value):
        return "高山駅"
    elif "松本" in str(value):
        return "松本駅"
    else:
        return value

class Options(scrapy.Item):
     depature = scrapy.Field(serializer = changeName)
     depatureTime = scrapy.Field()
     arrive = scrapy.Field(serializer = changeName)
     arriveTime = scrapy.Field()
     avaiable = scrapy.Field()
