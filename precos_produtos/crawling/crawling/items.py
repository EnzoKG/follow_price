# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from price.models import *

class PesquisaItem(DjangoItem):
    django_model = Pesquisa