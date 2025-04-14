from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By


class TestBrokenImages:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/broken_images')

	def teardown_method(self):
		self.driver.quit()

	def get_nth_image(self, index):
		return self.driver.find_elements(
			By.XPATH, '//div[@id="content"]//img'
		)[index]

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
