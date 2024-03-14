import scrapy


class HighwaybusSpider(scrapy.Spider):
    name = "HighwayBus"
    allowed_domains = ["www.highwaybus.com"]
    start_urls = ["https://www.highwaybus.com/gp/index"]

    def parse(self, response):
        pass
