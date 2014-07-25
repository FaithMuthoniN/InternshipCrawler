import scrapy
import time 
from selenium import webdriver 


class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		print response.body
		with open(filename, 'wb') as f:
			f.write(response.body)

class GoogleSpider(scrapy.Spider):
	name = "google"
	allowed_domains = ["google.com"]
	start_urls = [
		"https://www.google.com/about/careers/search"
	]

	def __init__(self):
		self.driver = webdriver.Firefox()

	def parse(self, response):
		self.driver.get(response.url)
		search_bar = self.driver.find_element_by_id("gbqfq")
		search_bar.send_keys("Summer")
		button = self.driver.find_element_by_class_name("gbqfb")
		button.click()

		while True:
			next_page = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/div/div[6]/a[4]/img")
			try:
				next_page.click()
				hxs = HtmlXPathSelector(response)
				print hxs
				titles = hxs.select("//span[@class='pl']")
				for title in titles:
					title = titles.select("a/text()").extract()
					link = titles.select("a/@href").extract()
					#print title, link
			except:
				break

		filename = "Google"
		with open(filename, 'wb') as f:
			f.write(response.body)


class FacebookSpider(scrapy.Spider):
	name = "facebook"
	allowed_domains = ["facebook.com"]
	start_urls = [
		"https://www.facebook.com/careers/university"
	]

	def parse(self, response):
		filename = "Facebook"
		with open(filename, 'wb') as f:
			f.write(response.body)


