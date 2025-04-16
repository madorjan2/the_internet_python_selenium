import os

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_test_data_path():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'test_data', 'test_data_17.txt')
	return path


class TestFileUpload(BaseTest):
	page_url = '/upload'

	def test_file_upload(self):
		self.wait.until(
			EC.element_to_be_clickable((By.ID, 'file-upload'))
		).send_keys(get_test_data_path())
		self.wait.until(
			EC.element_to_be_clickable((By.ID, 'file-submit'))
		).click()
		assert (
			self.wait.until(
				EC.visibility_of_element_located((By.ID, 'uploaded-files'))
			).text
			== 'test_data_17.txt'
		)
