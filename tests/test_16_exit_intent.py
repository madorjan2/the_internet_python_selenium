from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestExitIntent:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/exit_intent')

	def teardown_method(self):
		self.driver.quit()

	def test_exit_intent(self):
		# I have not found a way to simulate moving the cursor outside the browser window in headless mode
		# therefore I am triggering the event directly
		self.driver.execute_script('_ouibounce.fire()')
		WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="modal-footer"]/p'))).click()
		WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="modal-footer"]/p')))