import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ['https://books.toscrape.com']  # URL the spider should visit
    def parse(self, response):
        print("[ parse ]")
        
        # print(response.css("h3 a::text").get())
        
        ebooks = response.css("article.product_prod")
        for ebook in ebooks:
            #title = ebook.css("h3 a::attr[title]").get()
            title = ebook.css("h3 a").attrib[title]
            title = ebook.css("p.price_color::text").get()
            
            
            yield {
                "title": title,
                "price": price
            }