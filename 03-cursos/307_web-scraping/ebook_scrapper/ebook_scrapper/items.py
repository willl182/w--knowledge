from scrapy import Item, Field

class EbookItem(Item):
    title = Field()
    price = Field()