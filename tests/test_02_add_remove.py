from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By


class TestAddRemoveElement:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/add_remove_elements/')

	def teardown_method(self):
		self.driver.quit()

	def add_element(self):
		self.driver.find_element(
			By.XPATH, '//button[text()="Add Element"]'
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
