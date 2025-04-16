import os

from utils.create_driver import create_chrome_driver

from selenium.webdriver.support.wait import WebDriverWait


def clear_download_directory():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, '..', 'tests', 'downloads')
	for filename in os.listdir(path):
		file_path = os.path.join(path, filename)
		os.remove(file_path)

class BaseTest(object):
	page_url = None

	def setup_class(self):
		clear_download_directory()

	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080' + self.page_url)
		self.wait = WebDriverWait(self.driver, 5)

	def teardown_method(self):
		self.driver.quit()
