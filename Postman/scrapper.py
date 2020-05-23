from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

def spiders():
	setting = get_project_settings()
	process = CrawlerProcess(setting)
	print(process.spiders.list())
	for spider_name in process.spiders.list():
	    print ("Running spider %s" % (spider_name))
	    process.crawl(spider_name,query="dvh") #query dvh is custom argument used in your scrapy

	process.start()

