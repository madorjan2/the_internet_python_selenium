from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDynamicLoading(BaseTest):
	page_url = '/dynamic_loading'

	def test_hidden_element(self):
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Example 1'))
		).click()
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]'))
		).click()
		div_result = WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located((By.ID, 'finish'))
		)
		assert div_result.text == 'Hello World!'

	def test_not_present_element(self):
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Example 2'))
		).click()
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]'))
		).click()
		div_result = WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located((By.ID, 'finish'))
		)
		assert div_result.text == 'Hello World!'
