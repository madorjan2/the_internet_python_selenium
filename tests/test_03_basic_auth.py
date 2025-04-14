import base64
from utils.create_driver import create_chrome_driver_wired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

valid_auth = base64.encodebytes('admin:admin'.encode()).decode().strip()
invalid_auth = base64.encodebytes('something:other'.encode()).decode().strip()


def valid_interceptor(request):
	request.headers['Authorization'] = f'Basic {valid_auth}'


def invalid_interceptor(request):
	request.headers['Authorization'] = f'Basic {invalid_auth}'


class TestBasicAuth:
	def setup_method(self):
		self.driver = create_chrome_driver_wired()

	def teardown_method(self):
		self.driver.quit()

	def test_valid_login(self):
		self.driver.request_interceptor = valid_interceptor
		self.driver.get('http://localhost:7080/basic_auth')
		h3 = WebDriverWait(self.driver, 3).until(
			EC.visibility_of_element_located((By.TAG_NAME, 'h3'))
		)
		p = WebDriverWait(self.driver, 3).until(
			EC.visibility_of_element_located((By.TAG_NAME, 'p'))
		)
		assert h3.text == 'Basic Auth'
		assert (
			p.text == 'Congratulations! You must have the proper credentials.'
		)

	def test_invalid_login(self):
		self.driver.request_interceptor = invalid_interceptor
		self.driver.get('http://localhost:7080/basic_auth')
		assert len(self.driver.find_elements(By.TAG_NAME, 'h3')) == 0
