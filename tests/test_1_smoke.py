from ..utils.create_driver import create_chrome_driver

from selenium.webdriver.common.by import By

class TestAB:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080')

	def teardown_method(self):
		self.driver.quit()

	def test_title(self):
		assert self.driver.find_element(By.TAG_NAME, 'h1').text == 'Welcome to the-internet'
		assert len(self.driver.find_elements(By.TAG_NAME, 'li')) == 44