from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

class Spider(object):
	def __init__(self, headless=False):
		options = webdriver.ChromeOptions()
		if headless:
			options.add_argument('headless')
		self.browser = webdriver.Chrome(r'C:\webdriver\chromedriver', chrome_options=options)
		# self.browser = webdriver.PhantomJS(r'C:\webdriver\phantomjs')

	def wait_until_el(self, css_selector, time=10):
		try:
			element = WebDriverWait(self.browser, time).until(
					EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
				)
			return element
		except Exception as e:
			return None

	def stop(self):
		self.browser.quit()

	def elements(self, selector):
		return self.browser.find_elements_by_css_selector(selector)

	def element(self, selector):
		return self.browser.find_element_by_css_selector(selector)

	def click(self, element):
		element.click()

	def get_time(self):
		return str(datetime.now().strftime('%d-%m-%Y %I:%M:%S'))

	def write_log_csv(self, data, file):
		f = open(file, 'a+')
		for i in range(len(data)): # makes sure evreything is str
			data[i] = str(data[i])
		f.write(','.join([self.get_time()] + data) + '\n')
		f.close()

	def write_log(self, line, file):
		f = open(file, 'a+')
		f.write(str(datetime.now().strftime('%d-%m-%Y %I:%M:%S')) + ',' + line  + '\n')
		f.close()
