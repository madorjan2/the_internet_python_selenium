from utils.base_test import BaseTest
from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TEST_DATA = {'latitude': 12.345, 'longitude': 9.8765, 'accuracy': 100}


class TestGeolocation(BaseTest):
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.execute_cdp_cmd('Page.setGeolocationOverride', TEST_DATA)
		self.driver.get('http://localhost:7080/geolocation')

	def test_geolocation(self):
		WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable((By.TAG_NAME, 'button'))
		).click()
		assert WebDriverWait(self.driver, 5).until(
			(EC.visibility_of_element_located((By.ID, 'lat-value')))
		).text == str(TEST_DATA['latitude'])
		assert WebDriverWait(self.driver, 5).until(
			(EC.visibility_of_element_located((By.ID, 'long-value')))
		).text == str(TEST_DATA['longitude'])
