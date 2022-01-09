import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DealsT2Spider(CrawlSpider):
    name = 'deals_t2'
    allowed_domains = ['www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY']
    start_urls = ['http://www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    
           
        

