from utils.create_driver import create_chrome_driver


class BaseTest(object):
	page_url = None

	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080' + self.page_url)

	def teardown_method(self):
		self.driver.quit()
