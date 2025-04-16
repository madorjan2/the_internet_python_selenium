from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class TestDisappearingElements(BaseTest):
	page_url = '/disappearing_elements'

	def is_gallery_present(self):
		try:
			self.wait.until(
				EC.element_to_be_clickable((By.LINK_TEXT, 'Gallery'))
			)
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
				counter += 1
			assert counter < 100
		else:
			counter = 0
			while not is_present and counter < 100:
				self.driver.refresh()
				is_present = self.is_gallery_present()
				counter += 1
			assert counter < 100
