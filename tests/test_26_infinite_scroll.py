from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.common import TimeoutException


class TestHovers(BaseTest):
	page_url = '/infinite_scroll'

	def get_num_of_paragraphs(self):
		return len(
			self.wait.until(
				EC.visibility_of_all_elements_located(
					(By.XPATH, '//div[@class="jscroll-added"]')
				)
			)
		)

	def test_scroll_by_page_down(self):
		for _ in range(10):
			orig_num = self.get_num_of_paragraphs()
			ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
			try:
				self.wait.until(
					lambda driver: self.get_num_of_paragraphs() > orig_num
				)
			except TimeoutException:
				raise AssertionError(
					'No new paragraph appeared upon scrolling to the bottom'
				)

	def test_scroll_by_javascript(self):
		for _ in range(10):
			orig_num = self.get_num_of_paragraphs()
			self.driver.execute_script(
				'window.scrollTo(0, document.body.scrollHeight);'
			)
			try:
				self.wait.until(
					lambda driver: self.get_num_of_paragraphs() > orig_num
				)
			except TimeoutException:
				raise AssertionError(
					'No new paragraph appeared upon scrolling to the bottom'
				)
