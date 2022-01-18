import scrapy 
from datetime import datetime
from ..items import MerclivreItem
from scrapy.loader import ItemLoader

class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.mercadolivre.com.br']

    def start_requests(self):
            yield scrapy.Request(url='https://www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY',callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }) 
            
    def parse(self, response):   
        deals = response.xpath("//div[@class='promotions_boxed-width']/div/ol/li")
        
        for deal in deals:
            loader = ItemLoader(item=MerclivreItem(),selector=deal, response=response)   
             
            loader.add_xpath("product_name", ".//a/div/div/p/text()")
            loader.add_xpath("original_price", ".//a/div/div/span[@class='promotion-item__oldprice']//text()")
            loader.add_xpath("current_price", ".//a/div/div/div[2]/span[@class='promotion-item__price']//text()")
            loader.add_xpath("product_url", ".//a/@href")
            loader._add_value("extraction_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            yield loader.load_item()
                
        next_page = response.xpath(
            "//li[@class='andes-pagination__button andes-pagination__button--next']/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse,headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            })