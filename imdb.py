#Selenium to scrapy all american movies from 1972-2016

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import urllib.request
i=0
file = open('movies.txt','a')
class allMovies(object):
	def __init__(self,i):
		self.i=i
		self.url = f"https://www.imdb.com/list/ls057823854/?sort=list_order,asc&st_dt=&mode=detail&page={i}"
		self.driver=webdriver.Chrome(ChromeDriverManager().install())
		self.delay= 2
	#to scrape all movie details in the current page
	def open_page(self):
		self.driver.get(self.url)
		try:
			wait=WebDriverWait(self.driver,self.delay) # a small delay of 2 seconds
			print("page is ready")
		except TimeoutException:
			print("loading timeout")

	def scrape_page(self):
		#all_list = self.driver.find_elements_by_class_name("lister-item-content")
		for link in self.driver.find_elements_by_class_name('lister-item-header'):
			l = link.text
			print(l)
			file.write(l)
			print(l[:3])
			print(l[3:-6])
			print(l[-6:-1])
	def quit(self):
		self.driver.close()
for i in range(1,3):
	scraper = allMovies(i)
	scraper.open_page()
	scraper.scrape_page()
	scraper.quit()


