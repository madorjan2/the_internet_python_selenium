from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestIframe:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/iframe')

	def teardown_method(self):
		self.driver.quit()

	def test_iframe(self):
		WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable(
				(By.XPATH, '//button[contains(@class, "tox-button")]')
			)
		).click()
		iframe = self.driver.find_element(By.ID, 'mce_0_ifr')
		self.driver.switch_to.frame(iframe)
		assert (
			self.driver.find_element(By.ID, 'tinymce').text
			== 'Your content goes here.'
		)
