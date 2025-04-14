from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNestedFrames:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/nested_frames')

	def teardown_method(self):
		self.driver.quit()

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
			EC.presence_of_element_located((By.NAME, f'frame-bottom'))
		)
		self.driver.switch_to.frame(frame)
		assert self.driver.find_element(By.TAG_NAME, 'body').text == 'BOTTOM'
