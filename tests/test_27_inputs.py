import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class TestInputs(BaseTest):
	page_url = '/inputs'

	def setup_method(self):
		super().setup_method()
		self.input_field = self.wait.until(
			EC.element_to_be_clickable((By.TAG_NAME, 'input'))
		)

	@pytest.mark.dependency()
	def test_accepts_input(self):
		self.input_field.send_keys('123')
		assert self.input_field.get_property('value') == '123'

	@pytest.mark.dependency(depends=['TestInputs::test_accepts_input'])
	def test_arrow_keys(self):
		self.input_field.send_keys('123')
		self.input_field.send_keys(Keys.ARROW_UP)
		assert self.input_field.get_property('value') == '124'
		self.input_field.send_keys(Keys.ARROW_DOWN)
		assert self.input_field.get_property('value') == '123'

	# ToDo (after multiple browser support implementation): negative branch is browser-dependant, since the accepted input differs (e.g. Firefox accepts all kind of input in number type fields)
