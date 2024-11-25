---
# Creating a Scrapy Spider
---

In this module, the focus is on building and refining a Scrapy spider for web scraping. Key concepts include:

1. **Scrapy Spider Creation**  
   - Learn how to build a basic Scrapy spider that sends requests to websites and handles responses.
   
2. **CSS Selectors for Data Extraction**  
   - Use CSS selectors to extract specific data from web pages efficiently.

3. **Request and Response Handling**  
   - Send HTTP requests within the spider and handle the server responses, enabling the spider to scrape the required data.

These skills enable the creation of a functional and customizable spider for web scraping tasks.

## Creating a Scrapy Spider

To start scraping websites with Scrapy, we need to create **spiders**. A spider is a Python class that defines how to scrape information from websites.

1. **Spider Definition**  
   - A spider class is defined within a Python file in the `spiders` folder of the Scrapy project.
   - Each spider contains details such as the website to scrape, the data to select, and how to extract the data.

2. **Inheriting from Scrapy Spider**  
   - To access built-in functionalities like sending requests, handling responses, and extracting data, the spider class must inherit from the `scrapy.Spider` class.

3. **Spider Structure**  
   - Import Scrapy and create a new class, inheriting from `scrapy.Spider`.
   - Define the spider's name using the `name` class variable.

#### Example Code to Create a Spider:

```python
import scrapy

class EbookSpider(scrapy.Spider):
    name = 'ebook'  # The name of the spider
    # Other configurations like start_urls, parsing methods, etc.
```

In this example, `EbookSpider` inherits from `scrapy.Spider` and defines the spider's name as `'ebook'`. This spider will handle the scraping logic, including the URL to scrape and the data to extract.


## Sending Requests in Scrapy

To scrape data, a spider needs to first **send a request** to a website to retrieve its content. Here’s how it's done:

1. **Defining Start URLs**  
   - The `start_urls` class variable is used to define the URL(s) that the spider should initially send requests to.
   - It stores a list of URLs, and Scrapy will send requests to those URLs when the spider starts.

2. **Scraping Example**  
   - For this example, we will scrape a test website (`books.toscrape.com`) and extract book titles and prices.

#### Example Code:

```python
class EbookSpider(scrapy.Spider):
    name = 'ebook'
    start_urls = ['https://books.toscrape.com']  # URL the spider should visit
```

In this example, the `start_urls` list contains the URL `https://books.toscrape.com`, where the spider will begin its scraping process. The spider will then send a request to this URL.


# Getting the Response in Scrapy

After sending a request, the next step is to **handle the response** from the website. Scrapy calls a method named `parse` when it receives the response.

1. **`parse` Method**  
   - The `parse` method is where the response object is provided. This method is automatically called when Scrapy receives a response after sending a request to the specified URL.
   - You can perform actions on the response here, such as extracting data.

2. **Handling the Response**  
   - You can print the response object to see the server's response, which typically includes a status code (e.g., `200` for success) and the requested URL.
   
#### Example Code:

```python
class EbookSpider(scrapy.Spider):
    name = 'ebook'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        print("[Our response:]")
        print(response)
```

In this example:
- The `parse` method receives the `response` object, and we print it to see the data returned from the request.
- When the spider runs, Scrapy sends a request to the URL in `start_urls`, and once the response is received, it is passed to the `parse` method for further processing.

3. **Running the Spider**  
   - To run the spider and see the output, use the command:
   ```bash
   scrapy crawl ebook
   ```
   This starts the spider and prints out the response, including the status code (e.g., `200 OK`) and URL.

## Using Scrapy CSS Selectors

After defining the spider, sending a request, and receiving the response, the next step is to **extract specific data** from the HTML content using CSS selectors. CSS selectors are used to pinpoint elements within the HTML structure of a webpage, allowing Scrapy to extract the desired data.

#### Key Concepts:
1. **CSS Selectors**:
   - A **CSS selector** is a pattern used to select elements from a webpage's HTML structure. It leverages HTML tags, attributes, and their hierarchy to target specific parts of a page.
   - For example, selecting a `<a>` (link) tag inside an `<h3>` (header) tag allows us to focus on a specific section of the HTML.

2. **Chrome Developer Tools**:
   - Use Chrome's Developer Tools to inspect the HTML structure of a webpage. This is helpful to identify the exact tags and attributes of the data you want to extract.
   - With the "Inspector Tool," you can hover over elements on the webpage to see their corresponding HTML.

3. **Extracting Data Using CSS Selectors in Scrapy**:
   - Use the `response` object, which contains the entire HTML structure of the webpage, along with the `.css()` method to extract data using CSS selectors.
   - The `.get()` method retrieves the content selected by the CSS selector.

#### Example Code:

```python
class EbookSpider(scrapy.Spider):
    name = 'ebook'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        # Use CSS selector to find the book title within <h3> and <a> tags
        title = response.css('h3 a::text').get()
        print('Book title:', title)
```

**Explanation**:
- `response.css('h3 a::text')`: 
  - `h3` targets the `<h3>` HTML tag.
  - `a` selects the `<a>` tag within the `<h3>` (nested selection).
  - `::text` selects the inner text of the `<a>` tag.
- `.get()` retrieves the first matching result.

4. **Running the Spider**:
   - To execute the spider, use the command:
   ```bash
   scrapy crawl ebook
   ```
   - This command will start the scraping process, extract the data specified in the `parse` method, and print the desired elements (like the book title).

#### Additional Points:
- You can use `::attr(attribute)` in CSS selectors to extract specific attributes, like `href` for links.
- When selecting multiple elements, you can use `.getall()` instead of `.get()` to retrieve a list of results.

### Next Steps:
The lesson indicates that extracting **multiple items** (like all book titles and their prices on a page) will be covered next, demonstrating how to handle data when there are multiple instances on a webpage (e.g., a list of products).


