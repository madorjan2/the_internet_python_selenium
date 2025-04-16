from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestFormAuthentication(BaseTest):
	page_url = '/login'

	def test_form_authentication(self):
		username, password = [
			elem.text
			for elem in self.wait.until(
				EC.visibility_of_all_elements_located((By.TAG_NAME, 'em'))
			)
		]
		self.wait.until(
			EC.element_to_be_clickable((By.ID, 'username'))
		).send_keys(username)
		self.wait.until(
			EC.element_to_be_clickable((By.ID, 'password'))
		).send_keys(password)
		self.wait.until(
			EC.element_to_be_clickable((By.TAG_NAME, 'button'))
		).click()
		assert (
			'You logged into a secure area!'
			in self.wait.until(
				EC.visibility_of_element_located((By.ID, 'flash-messages'))
			).text
		)
