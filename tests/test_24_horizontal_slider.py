from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class TestHorizontalSlider(BaseTest):
	page_url = '/horizontal_slider'

	def setup_method(self):
		super().setup_method()
		self.slider = self.wait.until(
			EC.element_to_be_clickable((By.TAG_NAME, 'input'))
		)

	def test_click_in_the_middle_by_rect(self):
		# move_to_element moves the cursor to the middle of the element
		ActionChains(self.driver).move_to_element(
			self.slider
		).click().perform()
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.ID, 'range'))
			).text
			== '2.5'
		)

	def test_cursor_keys(self):
		for i in range(10):
			expected_result = int(i * 0.5) if i % 2 == 0 else i * 0.5
			assert self.wait.until(
				EC.visibility_of_element_located((By.ID, 'range'))
			).text == str(expected_result)
			self.slider.send_keys(Keys.ARROW_RIGHT)
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.ID, 'range'))
			).text
			== '5'
		)

	def test_dragging(self):
		ActionChains(self.driver).move_to_element_with_offset(
			self.slider, self.slider.rect['width'] / 2 * -1, 0
		).click().perform()
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.ID, 'range'))
			).text
			== '0'
		)
		ActionChains(self.driver).click_and_hold().move_to_element_with_offset(
			self.slider, self.slider.rect['width'] / 2, 0
		).release().perform()
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.ID, 'range'))
			).text
			== '5'
		)
