from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestInputs(BaseTest):
	page_url = '/javascript_alerts'

	def get_result_text(self):
		return self.wait.until(
			EC.visibility_of_element_located((By.ID, 'result'))
		).text

	def test_simple_alert(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Alert"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.accept()
		assert self.get_result_text() == 'You successfuly clicked an alert'

	def test_confirm_alert_accept(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Confirm"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.accept()
		assert self.get_result_text() == 'You clicked: Ok'

	def test_confirm_alert_dismiss(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Confirm"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.dismiss()
		assert self.get_result_text() == 'You clicked: Cancel'

	def test_prompt_alert_with_text(self):
		message = 'You are indeed a JS prompt'
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Prompt"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.send_keys(message)
		alert.accept()
		assert self.get_result_text() == f'You entered: {message}'

	def test_prompt_alert_without_text(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Prompt"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.accept()
		assert self.get_result_text() == 'You entered:'

	def test_prompt_alert_dismiss(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Click for JS Prompt"]')
			)
		).click()
		alert = self.driver.switch_to.alert
		alert.dismiss()
		assert self.get_result_text() == 'You entered: null'
