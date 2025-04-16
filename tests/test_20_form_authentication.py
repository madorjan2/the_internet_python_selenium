from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormAuthentication(BaseTest):
	page_url = '/login'

	def test_form_authentication(self):
		username, password = [
			elem.text
			for elem in WebDriverWait(self.driver, 2).until(
				EC.visibility_of_all_elements_located((By.TAG_NAME, 'em'))
			)
		]
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.ID, 'username'))
		).send_keys(username)
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.ID, 'password'))
		).send_keys(password)
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.TAG_NAME, 'button'))
		).click()
		assert (
			'You logged into a secure area!'
			in WebDriverWait(self.driver, 2)
			.until(EC.visibility_of_element_located((By.ID, 'flash-messages')))
			.text
		)
