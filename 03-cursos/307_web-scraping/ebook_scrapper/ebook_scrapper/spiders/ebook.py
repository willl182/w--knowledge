import Scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ['https://books.toscrape.com']  # URL the spider should visit
    def parse(self, response):
        print('Our response:', response)