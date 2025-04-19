from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestNestedFrames(BaseTest):
	page_url = '/nested_frames'

	def switch_to_frame_with_name(self, name):
		target_frame = self.wait.until(EC.presence_of_element_located((By.NAME, name)))
		self.driver.switch_to.frame(target_frame)

	def get_body_text(self):
		return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).text

	def test_nested_frames(self):
		self.switch_to_frame_with_name('frame-top')
		self.switch_to_frame_with_name('frame-left')
		assert self.get_body_text() == 'LEFT'
		self.driver.switch_to.parent_frame()
		self.switch_to_frame_with_name('frame-middle')
		assert self.get_body_text() == 'MIDDLE'
		self.driver.switch_to.parent_frame()
		self.switch_to_frame_with_name('frame-right')
		assert self.get_body_text() == 'RIGHT'
		self.driver.switch_to.parent_frame()
		self.driver.switch_to.parent_frame()
		self.switch_to_frame_with_name('frame-bottom')
		assert self.get_body_text() == 'BOTTOM'