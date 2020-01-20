from billiard.context import Process
from celery import shared_task
from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from scrapy_app.spiders.company_crawler import CompanyCrawlerSpider


class CrawlerProcess(Process):
    def __init__(self, spider):
        Process.__init__(self)
        settings = get_project_settings()
        self.crawler = Crawler(spider.__class__, settings)
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.spider = spider

    def run(self):
        self.crawler.crawl(self.spider)
        reactor.run()


@shared_task
def task_company_crawl():
    spider = CompanyCrawlerSpider()
    crawler = CrawlerProcess(spider)
    crawler.start()
    crawler.join()
