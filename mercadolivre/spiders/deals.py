import scrapy
from datetime import datetime

class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.mercadolivre.com.br']

    def start_requests(self):
            yield scrapy.Request(url='https://www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY',callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }) 
            
    def parse(self, response):   
        # date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     
        deals = response.xpath("//div[@class='promotions_boxed-width']/div/ol/li")
        for deal in deals:
            original_price = ' '.join(deal.xpath(".//a/div/div/span[@class='promotion-item__oldprice']//text()").re(r'[\d.,]+')).replace('.','',1).replace(' ','.')
            current_price = ' '.join(deal.xpath(".//a/div/div/div[2]/span[@class='promotion-item__price']//text()").re(r'[\d.,]+')).replace('.','',1).replace(' ','.')
                            
            yield{
                'product_name': deal.xpath(".//a/div/div/p/text()").get(),
                'original_price': original_price,
                'current_price': current_price, 
                'product_url': deal.xpath(".//a/@href").get(), 
                'extraction-date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }