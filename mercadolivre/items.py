# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join


def clean_original_price(original_price):
    if original_price:
        return original_price.replace('R$','').replace('.','')
    return original_price


def clean_current_price(current_price):
    if current_price:
        return current_price.replace('R$','').replace('.','')
    return current_price
        

class MerclivreItem(scrapy.Item):
    product_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    original_price = scrapy.Field(
        input_processor = MapCompose(clean_original_price, str.strip),
        output_processor = TakeFirst()
    )
    current_price = scrapy.Field(
        input_processor = MapCompose(clean_current_price, str.strip),
        output_processor = Join('.')
    )
    product_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    extraction_date = scrapy.Field(
        output_processor = TakeFirst()
    )