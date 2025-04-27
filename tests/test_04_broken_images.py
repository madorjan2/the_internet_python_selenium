import time
import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By


class TestBrokenImages(BaseTest):
	page_url = '/broken_images'

	def get_nth_image(self, index, timeout=5):
		loaded = False
		start_time = time.monotonic()
		imgs = []
		while not loaded and time.monotonic() - start_time < timeout:
			imgs = self.driver.find_elements(
				By.XPATH, '//div[@id="content"]//img'
			)
			loaded = len(imgs) >= index + 1
		if not loaded:
			pytest.fail(f'Image not loaded in time with index {index}')
		return imgs[index]

	def test_first_image_is_broken(self):
		img = self.get_nth_image(0)
		loaded = self.driver.execute_script(
			'return arguments[0].complete && typeof arguments[0].naturalWidth != "undefined" && arguments[0].naturalWidth > 0',
			img,
		)
		assert not loaded

	def test_second_image_is_broken(self):
		img = self.get_nth_image(1)
		loaded = self.driver.execute_script(
			'return arguments[0].complete && typeof arguments[0].naturalWidth != "undefined" && arguments[0].naturalWidth > 0',
			img,
		)
		assert not loaded

	def test_third_image_is_not_broken(self):
		img = self.get_nth_image(2)
		loaded = self.driver.execute_script(
			'return arguments[0].complete && typeof arguments[0].naturalWidth != "undefined" && arguments[0].naturalWidth > 0',
			img,
		)
		assert loaded
