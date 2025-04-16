from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestInputs(BaseTest):
	page_url = '/inputs'

	def setup_method(self):
		super().setup_method()
		self.input_field = WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable((By.TAG_NAME, 'input'))
		)

	def test_input_value(self):
		self.input_field.send_keys('123')
		assert self.input_field.get_property('value') == '123'
