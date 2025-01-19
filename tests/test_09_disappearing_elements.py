from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class TestDisappearingElements:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/disappearing_elements')

	def teardown_method(self):
		self.driver.quit()

	def is_gallery_present(self):
		try:
			WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Gallery')))
			return True
		except TimeoutException:
			return False

	def test_reload(self):
		is_present = self.is_gallery_present()
		if is_present:
			counter = 0
			while is_present and counter < 100:
				self.driver.refresh()
				is_present = self.is_gallery_present()
			assert counter < 100
		else:
			counter = 0
			while not is_present and counter < 100:
				self.driver.refresh()
				is_present = self.is_gallery_present()
			assert counter < 100
			
