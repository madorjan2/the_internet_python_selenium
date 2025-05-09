import os
import time
import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_downloaded_data(timeout=5, polling_interval=0.2):
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'downloads', 'some-file.txt')
	start_time = time.monotonic()
	while not os.path.exists(path) and time.monotonic() - start_time < timeout:
		time.sleep(polling_interval)
	if not os.path.exists(path):
		raise FileNotFoundError(f'File could not be found: {path}')
	else:
		with open(path, 'r') as f:
			return f.read()


def get_test_data():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'test_data', 'test_data_17.txt')
	with open(path, 'r') as f:
		return f.read()


class TestFileDownload(BaseTest):
	page_url = '/download'

	@pytest.mark.xdist_group(name='sequential')
	def test_file_download(self):
		self.wait.until(
			EC.element_to_be_clickable((By.LINK_TEXT, 'some-file.txt'))
		).click()
		assert get_downloaded_data() == get_test_data()
