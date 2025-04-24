import os
import time

import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def is_file_present_in_downloads(filename):
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'downloads', filename)
	return os.path.exists(path)


def is_file_downloaded(filename, timeout=5, poll_frequency=0.1):
	start_time = time.monotonic()
	while time.monotonic() < start_time + timeout:
		if is_file_present_in_downloads(filename):
			return True
		time.sleep(poll_frequency)
	return False


class TestJQueryMenus(BaseTest):
	page_url = '/jqueryui/menu'

	# we get ElementClickIntercepted if we try to click regularly, therefore Javascript clicking is necessary
	def click_jquery_element_by_id(self, element_id):
		button = self.wait.until(
			EC.element_to_be_clickable((By.ID, element_id))
		)
		self.driver.execute_script('arguments[0].click();', button)

	# in the JQuery menu, the button is considered enabled by Selenium even when disabled
	def test_first_button_is_disabled(self):
		disabled_button_parent = self.wait.until(
			EC.visibility_of_element_located(
				(By.XPATH, '//a[@id="ui-id-1"]/..')
			)
		)
		assert 'ui-state-disabled' in disabled_button_parent.get_attribute(
			'class'
		)

	@pytest.mark.parametrize(
		'file_type, element_id',
		[
			('menu.pdf', 'ui-id-6'),
			('menu.csv', 'ui-id-7'),
			('menu.xls', 'ui-id-8'),
		],
	)
	def test_download_file(self, file_type, element_id):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-4')
		self.click_jquery_element_by_id(element_id)
		assert is_file_downloaded(file_type)

	def test_back_to_jquery(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-5')
		assert self.driver.current_url == 'http://localhost:7080/jqueryui'
