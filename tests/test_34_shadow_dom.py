from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestShadowDOM(BaseTest):
	page_url = '/shadowdom'

	def test_open_shadow_dom(self):
		shadow_hosts = self.wait.until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'my-paragraph'))
		)

		shadow_root_1 = shadow_hosts[0].shadow_root
		assert (
			shadow_root_1.find_element(By.CSS_SELECTOR, 'p').text
			== "Let's have some different text!"
		)
