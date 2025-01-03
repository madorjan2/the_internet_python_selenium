from selenium import webdriver
from selenium.webdriver import ChromeOptions

def create_chrome_driver(dev_mode=False):
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	if not dev_mode:
		options.add_argument('--headless')
	driver = webdriver.Chrome(options)
	driver.maximize_window()
	return driver