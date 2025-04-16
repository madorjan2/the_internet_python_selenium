from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestIframe(BaseTest):
	page_url = '/iframe'

	def test_iframe(self):
		WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[contains(@class, "tox-button")]')
			)
		).click()
		iframe = self.driver.find_element(By.ID, 'mce_0_ifr')
		self.driver.switch_to.frame(iframe)
		assert (
			self.driver.find_element(By.ID, 'tinymce').text
			== 'Your content goes here.'
		)
