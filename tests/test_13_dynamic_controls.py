from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDynamicControls:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/dynamic_controls')

	def teardown_method(self):
		self.driver.quit()

	def test_disappearing_checkbox(self):
		WebDriverWait(self.driver, 2).until(
			EC.visibility_of_element_located((By.ID, 'checkbox'))
		)
		button_toggle_checkbox = WebDriverWait(self.driver, 2).until(
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
		input_field = WebDriverWait(self.driver, 2).until(
			EC.visibility_of_element_located(
				(By.XPATH, '//form[@id="input-example"]//input')
			)
		)
		assert not input_field.is_enabled()
		button_toggle_input = WebDriverWait(self.driver, 2).until(
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
