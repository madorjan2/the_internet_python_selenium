import pytest

from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class TestDropdown(BaseTest):
	page_url = '/dropdown'

	def test_dropdown(self):
		my_select = Select(
			WebDriverWait(self.driver, 2).until(
				EC.element_to_be_clickable((By.ID, 'dropdown'))
			)
		)
		assert (
			my_select.first_selected_option.text == 'Please select an option'
		)
		my_select.select_by_index(1)
		assert my_select.first_selected_option.text == 'Option 1'
		my_select.select_by_value('2')
		assert my_select.first_selected_option.text == 'Option 2'
		with pytest.raises(NotImplementedError):
			my_select.select_by_visible_text('Please select an option')
