import pytest
from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestDropdown:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/dropdown')

	def teardown_method(self):
		self.driver.quit()

	def test_dropdown(self):
		my_select = Select(WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'dropdown'))))
		assert my_select.first_selected_option.text == 'Please select an option'
		my_select.select_by_index(1)
		assert my_select.first_selected_option.text == 'Option 1'
		my_select.select_by_value('2')
		assert my_select.first_selected_option.text == 'Option 2'
		with pytest.raises(NotImplementedError):
			my_select.select_by_visible_text('Please select an option')