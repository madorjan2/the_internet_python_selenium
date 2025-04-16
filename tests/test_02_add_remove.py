from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestAddRemoveElement(BaseTest):
	page_url = '/add_remove_elements/'

	def add_element(self):
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[text()="Add Element"]')
			)
		).click()

	def get_number_of_elements(self):
		return len(
			self.driver.find_elements(
				By.XPATH, '//div[@id="elements"]//button'
			)
		)

	def delete_first_element(self):
		self.driver.find_elements(By.XPATH, '//div[@id="elements"]//button')[
			0
		].click()

	def test_add_element(self):
		self.add_element()
		assert self.get_number_of_elements() == 1
		self.add_element()
		self.add_element()
		assert self.get_number_of_elements() == 3

	def test_delete_button(self):
		self.add_element()
		assert self.get_number_of_elements() == 1
		self.delete_first_element()
		assert self.get_number_of_elements() == 0
		self.add_element()
		self.add_element()
		assert self.get_number_of_elements() == 2
		self.delete_first_element()
		assert self.get_number_of_elements() == 1
		self.delete_first_element()
		assert self.get_number_of_elements() == 0
