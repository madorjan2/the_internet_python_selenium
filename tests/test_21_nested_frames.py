from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNestedFrames(BaseTest):
	page_url = '/nested_frames'

	def test_nested_frames(self):
		frame_top = WebDriverWait(self.driver, 5).until(
			EC.presence_of_element_located((By.NAME, 'frame-top'))
		)
		self.driver.switch_to.frame(frame_top)

		for direction in ['left', 'middle', 'right']:
			frame = WebDriverWait(self.driver, 5).until(
				EC.presence_of_element_located((By.NAME, f'frame-{direction}'))
			)
			self.driver.switch_to.frame(frame)
			assert (
				self.driver.find_element(By.TAG_NAME, 'body').text
				== direction.upper()
			)
			self.driver.switch_to.parent_frame()

		self.driver.switch_to.parent_frame()
		frame = WebDriverWait(self.driver, 5).until(
			EC.presence_of_element_located((By.NAME, 'frame-bottom'))
		)
		self.driver.switch_to.frame(frame)
		assert self.driver.find_element(By.TAG_NAME, 'body').text == 'BOTTOM'
