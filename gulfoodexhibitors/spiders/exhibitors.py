import scrapy


class ExhibitorsSpider(scrapy.Spider):
    name = "exhibitors"
    allowed_domains = ["gulfood.com"]
    start_urls = ["https://gulfood.com"]

    def parse(self, response):
        pass
