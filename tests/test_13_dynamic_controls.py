from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDynamicControls(BaseTest):
	page_url = '/dynamic_controls'

	def test_disappearing_checkbox(self):
		self.wait.until(EC.visibility_of_element_located((By.ID, 'checkbox')))
		button_toggle_checkbox = self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//form[@id="checkbox-example"]//button')
			)
		)
		button_toggle_checkbox.click()
		WebDriverWait(self.driver, 10).until(
			EC.invisibility_of_element_located((By.ID, 'checkbox'))
		)
		button_toggle_checkbox.click()
		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located((By.ID, 'checkbox'))
		)

	def test_disabled_input(self):
		input_field = self.wait.until(
			EC.visibility_of_element_located(
				(By.XPATH, '//form[@id="input-example"]//input')
			)
		)
		assert not input_field.is_enabled()
		button_toggle_input = self.wait.until(
			EC.visibility_of_element_located(
				(By.XPATH, '//form[@id="input-example"]//button')
			)
		)
		button_toggle_input.click()
		WebDriverWait(self.driver, 10).until(
			EC.element_to_be_clickable(
				(By.XPATH, '//form[@id="input-example"]//input')
			)
		)
		assert input_field.is_enabled()
		button_toggle_input.click()
		input_field = WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located(
				(By.XPATH, '//form[@id="input-example"]//input[@disabled]')
			)
		)
		assert not input_field.is_enabled()
