import os

from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_test_data_path():
	this_folder_path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
	path = os.path.join(this_folder_path, 'test_data', 'test_data_17.txt')
	return path

class TestFileUpload:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/upload')

	def teardown_method(self):
		self.driver.quit()

	def test_file_upload(self):
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'file-upload'))).send_keys(get_test_data_path())
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'file-submit'))).click()
		assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'uploaded-files'))).text == 'test_data_17.txt'
