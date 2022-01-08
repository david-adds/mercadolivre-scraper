import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY']
    start_urls = ['http://www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY/']

    def parse(self, response):
        pass
