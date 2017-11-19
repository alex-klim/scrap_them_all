import scrapy
from habr_lua.items import HabrLuaItem


class HabrSpider(scrapy.Spider):
    name = 'lua_spider'
    start_urls = ['https://habrahabr.ru/hub/lua/all/']
    posts = []

    def get_properties(self, response):
        post = HabrLuaItem()
        post['author'] = response.xpath(
            '//span[@class="user-info__nickname user-info__nickname_small"]/text()'
        ).extract()

        post['date'] = response.xpath(
            '//span[@class="post__time"]/text()'
        ).extract()

        post['hubs'] = response.xpath(
            '//li[@class="inline-list__item inline-list__item_hub"]/a/text()'
        ).extract()

        post['type_label'] = response.xpath(
            '//span[@class="post__type-label"]/text()'
        ).extract()

        post['text'] = " ".join("".join(response.xpath(
            '//div[@class="post__text post__text-html js-mediator-article"]/descendant-or-self::text()'
        ).extract()).split())

        post['image'] = response.xpath(
            '//div[@class="post__body post__body_full"]//img/@src'
        ).extract()

        post['tag'] = response.xpath(
            '//li[@class="inline-list__item inline-list__item_tag"]/a/text()'
        ).extract()

        post['rating'] = response.xpath(
            '//div[@class="voting-wjt voting-wjt_post js-post-vote"]/span/text()'
        ).extract()

        post['bookmarks'] = response.xpath(
            '//span[@class="bookmark__counter js-favs_count"]/text()'
        ).extract()

        post['views'] = response.xpath(
            '//span[@class="post-stats__views-count"]/text()'
        ).extract()

        post['comments_count'] = response.xpath(
            '//span[@class="post-stats__comments-count"]/text()'
        ).extract()

        yield post

    def parse(self, response):
        posts = response.xpath('//h2[@class="post__title"]/a/@href').extract()
        for post in posts:
            yield scrapy.Request(post, callback=self.get_properties)

        for next_page in response.xpath('//li[@class="arrows-pagination__item"]/a[@id="next_page"]/@href'):
            yield response.follow(next_page, self.parse)

