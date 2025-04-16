import os
import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


def create_download_directory():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'downloads')

class TestInputs(BaseTest):
	page_url = '/jqueryui/menu'

	def setup_method(self):
		super().setup_method()
		create_download_directory()