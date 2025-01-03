from selenium import webdriver
from selenium.webdriver import ChromeOptions
from seleniumwire import webdriver as wiredriver

def create_chrome_driver(dev_mode=False):
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	if not dev_mode:
		options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)
	driver.maximize_window()
	return driver

def create_chrome_driver_wired(dev_mode=False):
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	if not dev_mode:
		options.add_argument('--headless')
	driver = wiredriver.Chrome(options=options)
	driver.maximize_window()
	return driver