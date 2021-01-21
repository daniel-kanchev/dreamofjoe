import scrapy


class JoeSpider(scrapy.Spider):
    name = 'joe'
    allowed_domains = ['dreamofjoe.com']
    start_urls = ['https://dreamofjoe.com/']

    def parse(self, response):
        pass
