import scrapy

class ForumSpider(scrapy.Spider):
    name = 'forum_spider'
    start_urls = ['https://www.guanwuxiaoer.com/forum-chukou-1.html']  # 替换为目标论坛的起始URL

    def parse(self, response):
        # 解析问题链接并发送请求
        question_links = response.xpath('//a[@class="question-link"]/@href').getall()
        for link in question_links:
            yield response.follow(link, callback=self.parse_question)

        # 翻页逻辑，继续爬取下一页
        next_page = response.xpath('//a[@class="next-page"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_question(self, response):
        # 解析问题和回答内容
        question = response.xpath('//h1/text()').get()
        answers = response.xpath('//div[@class="answer"]/text()').getall()

        # 在这里可以进行数据存储或其他处理操作
        # ...

        # 输出问题和回答内容
        print('Question:', question)
        print('Answers:', answers)
