from datetime import datetime

from utils.create_driver import create_chrome_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


locators = [
	('ID', By.ID, 'sibling-50.3'),
	('XPATH ID', By.XPATH, '//div[@id="sibling-50.3"]'),
	('Absolute XPATH', By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[3]/div[2]')
]

def get_locator_performances():
	driver = create_chrome_driver()
	driver.get('http://localhost:7080/large')
	WebDriverWait(driver, 5).until(EC.visibility_of_element_located((locators[0][1], locators[0][2])))

	results = {}
	for name, by, value in locators:
		start_time = datetime.now()
		driver.find_element(by, value)
		end_time = datetime.now()
		results[name] = (end_time - start_time).microseconds

	return results

if __name__ == '__main__':
	print(get_locator_performances())