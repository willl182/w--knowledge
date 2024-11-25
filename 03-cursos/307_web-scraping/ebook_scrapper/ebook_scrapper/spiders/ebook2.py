import scrapy

class EbookSpider(scrapy.Spider):''
    name = "ebook2"
    start_urls = ['https://books.toscrape.com']  # URL the spider should visit
    def parse(self, response):
        print("[ parse ]")
        
        #print("CSS: ",response.css("h3 a::text")[0])
        
        
        
        #print("CSS based on class: ",response.css(".price_color::text").get()) #se usa el punto para seleccionar una clase
        #print("CSS based on id: ",response.css("#messages").get()) #se usa el # para seleccionar un id
        #print(response.css("a[title]").get()) #seleccionar por atributo dentro del elemento web
        #print(response.css("a[title = 'Soumission']").get()) #seleccionar por atributo dentro del elemento web 

        print("XPath: ",response.xpath("//h3/")[0])