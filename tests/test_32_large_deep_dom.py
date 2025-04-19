from utils.base_test import BaseTest
from utils.locator_performance import find_fastest_locator

from selenium.webdriver.common.by import By


div_locators = {
	'direct': [
		{'name': 'ID', 'by': By.ID, 'value': 'sibling-50.3'},
		{
			'name': 'XPATH TAG + ID',
			'by': By.XPATH,
			'value': '//div[@id="sibling-50.3"]',
		},
		{
			'name': 'XPATH WILDCARD + ID',
			'by': By.XPATH,
			'value': '//*[@id="sibling-50.3"]',
		},
		{
			'name': 'Absolute XPATH',
			'by': By.XPATH,
			'value': '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[2]',
		},
		{
			'name': 'XPATH TAG + Text',
			'by': By.XPATH,
			'value': '//div[text()="50.3"]',
		},
		{
			'name': 'XPATH WILDCARD + Text',
			'by': By.XPATH,
			'value': '//*[text()="50.3"]',
		},
	],
	'indirect': [
		{'name': 'TAGNAME', 'by': By.TAG_NAME, 'value': 'div', 'index': 258}
	],
	'url': 'http://localhost:7080/large',
	'expected': '50.3',
}


# as there is not much to test here, let's figure out the fastest locator strategies
class TestLargeDeepDOMs(BaseTest):
	page_url = '/large'

	def test_deep_dom(self):
		by, value = find_fastest_locator(div_locators)
		assert self.driver.find_element(by, value).text == '50.3'
