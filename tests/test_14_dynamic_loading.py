from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDynamicLoading:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/dynamic_loading')

	def teardown_method(self):
		self.driver.quit()

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
