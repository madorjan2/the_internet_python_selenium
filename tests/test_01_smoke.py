from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestSmoke(BaseTest):
	page_url = ''

	def test_title(self):
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
			).text
			== 'Welcome to the-internet'
		)
		assert len(self.driver.find_elements(By.TAG_NAME, 'li')) == 44
