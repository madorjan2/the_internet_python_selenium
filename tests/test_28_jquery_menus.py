import os
import time

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def is_file_present_in_downloads(filename):
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'downloads', filename)
	return os.path.exists(path)


def is_file_downloaded(filename):
	n_of_tries = 0
	while not is_file_present_in_downloads(filename) and n_of_tries < 50:
		n_of_tries += 1
		time.sleep(0.1)
	return is_file_present_in_downloads(filename)


class TestInputs(BaseTest):
	page_url = '/jqueryui/menu'

	def click_jquery_element_by_id(self, id):
		button = self.wait.until(EC.element_to_be_clickable((By.ID, id)))
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

	# we get ElementClickIntercepted if we try to click regularly, therefore Javascript clicking is necessary
	def test_download_pdf(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-4')
		self.click_jquery_element_by_id('ui-id-6')
		assert is_file_downloaded('menu.pdf')

	def test_download_csv(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-4')
		self.click_jquery_element_by_id('ui-id-7')
		assert is_file_downloaded('menu.csv')

	def test_download_excel(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-4')
		self.click_jquery_element_by_id('ui-id-8')
		assert is_file_downloaded('menu.xls')

	def test_back_to_jquery(self):
		self.click_jquery_element_by_id('ui-id-2')
		self.click_jquery_element_by_id('ui-id-5')
		assert self.driver.current_url == 'http://localhost:7080/jqueryui'
