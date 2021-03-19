import scrapy
from crawling.items import *
from price.models import *
import re

class PichauSpider(scrapy.Spider):
    name = 'Pichau'
    allowed_domains = ['www.pichau.com.br']
    start_urls = ['https://www.pichau.com.br']

    def parse(self, response):
        try:
            url = response.url+"/cadeiras/gamer"
            yield scrapy.Request(url=url, callback=self.pegando_dados)
        except ValueError as error:
            print(error)
    
    def pegando_dados(self, response):
        try:
            id_list = response.xpath('//*[@id="narrow-by-list"]/dd[7]/form/ol//input/@value').getall()
            for id_ in id_list:
                url = response.url+"?marcas="+id_+"&product_list_limit=48"
                yield scrapy.Request(url=url, callback=self.pagina_pessoal)
        except ValueError as error:
            print(error)

    def pagina_pessoal(self, response):
        try:
            link_all = response.xpath('//*[@id="amasty-shopby-product-list"]/div[2]/ol//a/@href').getall()
            for link in link_all:
                yield scrapy.Request(url=link, callback=self.valores)
        except ValueError as error:
            print(error)

    def valores(self, response):
        try:
            pesquisa = PesquisaItem()
            preco_parcelado = response.css('span.price::text').get()
            preco_boleto = response.css('span.price-boleto::text').get()
            titulo = response.css('div.product.title > h1::text').get()

            pesquisa['titulo'] = titulo
            pesquisa['preco_parcelado'] = preco_parcelado
            pesquisa['preco_boleto'] = preco_boleto
            
            pesquisa.save()
        except ValueError as error:
            print(error)