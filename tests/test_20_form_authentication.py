from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestFormAuthentication:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/login')

	def teardown_method(self):
		self.driver.quit()

	def test_form_authentication(self):
		username, password = [elem.text for elem in WebDriverWait(self.driver, 2).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'em')))]
		WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(username)
		WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(password)
		WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
		assert 'You logged into a secure area!' in WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'flash-messages'))).text

