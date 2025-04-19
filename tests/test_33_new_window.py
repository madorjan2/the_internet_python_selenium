from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestNewWindow(BaseTest):
	page_url = '/windows'

	def test_new_window(self):
		self.wait.until(
			EC.element_to_be_clickable((By.LINK_TEXT, 'Click Here'))
		).click()

		# Despite opening a new window, Selenium stays on the old window
		assert self.driver.current_url == self.base_url + self.page_url
		assert len(self.driver.window_handles) == 2

		# We have to switch to the new window to work with that
		self.driver.switch_to.window(self.driver.window_handles[1])
		assert (
			self.driver.current_url == self.base_url + self.page_url + '/new'
		)
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.TAG_NAME, 'h3'))
			).text
			== 'New Window'
		)

		# If we close the current window, we still have to switch back to the old window, otherwise we get NoSuchWindowException
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		assert self.driver.current_url == self.base_url + self.page_url
		assert len(self.driver.window_handles) == 1
