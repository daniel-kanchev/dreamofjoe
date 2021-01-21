import scrapy
from datetime import datetime
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from dreamofjoe.items import Article


class JoeSpider(scrapy.Spider):
    name = 'joe'
    allowed_domains = ['dreamofjoe.com']
    start_urls = ['https://dreamofjoe.com/']

    def parse(self, response):
        article_links = response.xpath("//a[@class='more-link']/@href").getall()
        yield from response.follow_all(article_links, self.parse_article)

        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        item = ItemLoader(Article(), response)
        item.default_output_processor = TakeFirst()

        title = response.xpath("//h1/a/text()").get()

        categories = response.xpath("//div[@class='post-category']/a/text()").getall()
        categories = [category.capitalize() for category in categories]
        categories = ", ".join(categories)

        date = response.xpath("//span[@itemprop='datePublished']/@content").get()
        date_time_obj = datetime.strptime(date, '%d/%m/%Y')
        date = date_time_obj.strftime("%Y/%m/%d")

        content = response.xpath("//article/p/text()").getall()
        if not content:
            content = response.xpath("//article[@class='post-content entry-content']"
                                     "/descendant-or-self::*/text()").getall()

        content = "\n".join(content)

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('categories', categories or "No text found in the article body")
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
