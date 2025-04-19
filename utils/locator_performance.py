from datetime import datetime
from pprint import pprint

from utils.create_driver import create_chrome_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


example_locators = {
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


def get_locator_performances(locators, driver=None):
	if driver is None:
		driver = create_chrome_driver()
		driver.get(locators['url'])
	WebDriverWait(driver, 5).until(
		EC.visibility_of_element_located(
			(locators['direct'][0]['by'], locators['direct'][0]['value'])
		)
	)

	for i, direct_locator in enumerate(locators['direct']):
		start_time = datetime.now()
		assert (
			driver.find_element(
				direct_locator['by'], direct_locator['value']
			).text
			== locators['expected']
		)
		end_time = datetime.now()
		locators['direct'][i]['time'] = (end_time - start_time).microseconds

	for i, indirect_locator in enumerate(locators['indirect']):
		start_time = datetime.now()
		assert (
			driver.find_elements(
				indirect_locator['by'], indirect_locator['value']
			)[indirect_locator['index']].text
			== locators['expected']
		)
		end_time = datetime.now()
		locators['indirect'][i]['time'] = (end_time - start_time).microseconds

	return locators


def find_fastest_locator(locators):
	locators = get_locator_performances(locators)
	best_locator = min(
		locators['direct'] + locators['indirect'],
		key=lambda item: item['time'],
	)
	return best_locator['by'], best_locator['value']


if __name__ == '__main__':
	example_locators = get_locator_performances(example_locators)
	pprint(example_locators)
	print(f'Best locator: {find_fastest_locator(example_locators)}')
