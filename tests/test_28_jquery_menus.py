import os

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class TestInputs(BaseTest):
	page_url = '/jqueryui/menu'

	def test_download_pdf(self):
		assert True