import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import Scrapy1Item

class W3SchoolsSpider(scrapy.Spider):
    name = "w3schools"
    allowed_domains = ["w3schools.com"]
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # Extract the title from the homepage
        title = response.css('title::text').get()

        # Extract the link to the HTML Tutorial page
        html_tutorial_link = response.xpath('//a[text()="HTML Tutorial"]/@href').get()

        # Follow the link to the HTML Tutorial page
        yield response.follow(html_tutorial_link, callback=self.parse_html)

    def parse_html(self, response):
        # Extract the title from the HTML Tutorial page
        html_title = response.css('title::text').get()

        # Extract all text within the <div class="w3-example"> element
        example_content = response.css('div.w3-example ::text').getall()

        # Join the extracted text to form a single string
        first_example = ' '.join(example_content).strip()

        # Store the extracted data in the Scrapy1Item item
        items = Scrapy1Item()
        items['html_title'] = html_title
        items['html_first_example'] = first_example

        yield items

        # Extract the link to the CSS Tutorial page
        css_tutorial_link = response.xpath('//a[text()="CSS Tutorial"]/@href').get()

        # Follow the link to the CSS Tutorial page
        yield response.follow(css_tutorial_link, callback=self.parse_css)

    def parse_css(self, response):
        # Extract the title from the CSS Tutorial page
        css_title = response.css('title::text').get()

        # Extract all text within the <div class="w3-example"> element
        example_content = response.css('div.w3-example ::text').getall()

        # Join the extracted text to form a single string
        first_example = ' '.join(example_content).strip()

        # Store the extracted data in the Scrapy1Item item
        items = Scrapy1Item()
        items['css_title'] = css_title
        items['css_first_example'] = first_example

        yield items

        # Extract the link to the PHP Tutorial page
        php_tutorial_link = response.xpath('//a[text()="PHP Tutorial"]/@href').get()

        # Follow the link to the PHP Tutorial page
        yield response.follow(php_tutorial_link, callback=self.parse_php)

    def parse_php(self, response):
        # Extract the title from the PHP Tutorial page
        php_title = response.css('title::text').get()

        # Extract all text within the <div class="w3-example"> element
        example_content = response.css('div.w3-example ::text').getall()

        # Join the extracted text to form a single string
        first_example = ' '.join(example_content).strip()

        # Store the extracted data in the Scrapy1Item item
        items = Scrapy1Item()
        items['php_title'] = php_title
        items['php_first_example'] = first_example

        yield items
