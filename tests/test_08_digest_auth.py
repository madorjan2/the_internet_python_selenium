from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDigestAuth:
	def setup_method(self):
		self.driver = create_chrome_driver()

	def teardown_method(self):
		self.driver.quit()

	def test_context_menu_positive(self):
		self.driver.get('http://admin:admin@localhost:7080/digest_auth')
		assert (
			WebDriverWait(self.driver, 5)
			.until(EC.visibility_of_element_located((By.TAG_NAME, 'h3')))
			.text
			== 'Digest Auth'
		)

	def test_context_menu_wrong_password(self):
		self.driver.get(
			'http://admin:nottherightpassword@localhost:7080/digest_auth'
		)
		assert len(self.driver.find_elements(By.TAG_NAME, 'h3')) == 0
