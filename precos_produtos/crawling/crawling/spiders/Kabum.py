import scrapy
from crawling.items import *
from price.models import *

class KabumSpider(scrapy.Spider):
    name = 'Kabum'
    allowed_domains = ['kabum.com.br']
    start_urls = ['https://www.kabum.com.br/']

    def parse(self, response):
        try:
            url = "https://www.kabum.com.br/gamer"
            yield scrapy.Request(url=url, callback=self.pegando_dados)
        except ValueError as error:
            print(error)
    
    def pegando_dados(self, response):
        try:
            equipamentos = Equipamentos.objects.all()
            for equipamento in equipamentos:
                if equipamento.titulo == "Cadeiras Gamer":    
                    link_produto = ""
                    yield scrapy.Request(url=link, callback=self.extraindo_dados)
                else:
                    print(equipamento.titulo)
        except ValueError as error:
            print(error)

    def extraindo_dados(self, response):
        try:
            titulo = response.xpath('//*[@id="img_fundo"]').get()
            print(str(titulo))
        except ValueError as error:
            print(error)