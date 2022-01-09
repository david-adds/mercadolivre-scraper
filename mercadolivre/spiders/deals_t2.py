import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime


class DealsSpider(CrawlSpider):
    name = 'deals_t2'

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.mercadolivre.com.br/ofertas?promotion_type=DEAL_OF_THE_DAY', headers={
            'User-Agent': self.user_agent
        })
        
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='promotions_boxed-width']/div/ol/li"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='andes-pagination__button andes-pagination__button--next']/a"),  process_request='set_user_agent'),

    )

    def set_user_agent(self,request,spider):
        request.headers['User-Agent'] = self.user_agent
        return request
    
    def parse_item(self, response):
        original_price = ''.join(response.xpath("//s[@class='price-tag ui-pdp-price__part ui-pdp-price__original-value price-tag__disabled']/span[@class='price-tag-amount']//text()").re(r'[\d.,]+')).replace('.','').replace(',','.'),
        current_price = ''.join(response.xpath("//div[@class='ui-pdp-price__second-line']/span/span[@class='price-tag-amount']//text()").re(r'[\d.,]+')).replace('.','').replace(',','.')
        yield {
            'product_name': response.xpath("//h1[@class='ui-pdp-title']/text()").get(),
            'original_price': original_price,
            'current_price': current_price,
            'product_url': response.url,
            'extraction-date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
           
        

