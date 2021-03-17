import scrapy


class KabumSpider(scrapy.Spider):
    name = 'Kabum'
    allowed_domains = ['www.kabum.com.br']
    start_urls = ['http://www.kabum.com.br/']

    def parse(self, response):
        pass
