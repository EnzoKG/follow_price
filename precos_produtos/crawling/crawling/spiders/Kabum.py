import scrapy
from crawling.items import *
from price.models import *
import re

class KabumSpider(scrapy.Spider):
    name = 'Kabum'
    allowed_domains = ['kabum.com.br']
    start_urls = ['https://www.kabum.com.br']

    def parse(self, response):
        try:
            equipamentos = Equipamentos.objects.all()
            for equipamento in equipamentos:   
                link_produto = response.url+equipamento.url
                yield scrapy.Request(url=link_produto, callback=self.pegando_dados)
        except ValueError as error:
            print(error)
    
    def pegando_dados(self, response):
        try:
            preco_normal = response.xpath('//*[@id="pag-detalhes"]/div[2]/div[2]/div[2]/div[1]/div[1]/text()').get()
            if preco_normal:
                preco_formatado = re.sub(r"\s+", "", str(preco_normal))
                print(preco_formatado)
            else:
                preco_desconto = response.xpath('//*[@id="pag-detalhes"]/div[2]/div[2]/div[3]/div[1]/span/span/text()').get()
                preco_formatado = re.sub(r"\s+", "", str(preco_desconto))
                print(preco_formatado)
        except ValueError as error:
            print(error)