# Acompanhamento de Preço
Este projeto tem o intuito de realizar a construção de uma aplicação web usando Django e Python para o acompanhamento de preços de equipamentos de grandes empresas.

## Neste projeto podemos encontrar as pastas:
1. crawling: que é o projeto de crawling de informações da(s) página(s);
2. precos_produtos: é o projeto django para o desenvolvimento de um sistema web;
3. price: é um app (application) onde será criado a nossa app.

## Para instalar dependecias do projeto:
**...: cd precos_produtos**

**...: pip install -r dependences.txt**

## Para executar o crawling da página basta digitar no terminal:
**...: scrapy crawl nome_spider**

**OU**

**...: scrapy runspider nome_spider.py**

**...: scrapy runspider nome_spider.py --nolog**

## Para executar o servidor, basta digitar:
**...: python manage.py runserver**
