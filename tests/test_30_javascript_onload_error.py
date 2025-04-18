from utils.base_test import BaseTest
from utils.create_driver import create_chrome_driver_capturing_logs


class TestErrors(BaseTest):
	page_url = '/javascript_error'

	def setup_method(self):
		self.driver = create_chrome_driver_capturing_logs()

	def test_errors_on_main_page(self):
		self.driver.get('http://localhost:7080')
		log_entries = self.driver.get_log('browser')
		js_errors = [
			entry for entry in log_entries if entry['source'] == 'javascript'
		]
		assert len(js_errors) == 0

	def test_errors_on_onload_page(self):
		self.driver.get('http://localhost:7080' + self.page_url)
		log_entries = self.driver.get_log('browser')
		js_errors = [
			entry for entry in log_entries if entry['source'] == 'javascript'
		]
		assert len(js_errors) > 0
