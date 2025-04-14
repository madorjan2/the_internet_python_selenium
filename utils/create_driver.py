import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from seleniumwire import webdriver as wiredriver

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
path = os.path.abspath(os.path.join(path, os.pardir, 'tests', 'downloads'))
if not os.path.exists(path):
	os.makedirs(path)


def create_chrome_driver(dev_mode=False):
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	options.add_experimental_option(
		'prefs',
		{
			'download.default_directory': path,
			'download.prompt_for_download': False,
			'download.directory_upgrade': True,
			'safebrowsing.enabled': True,
		},
	)
	if not dev_mode:
		options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)
	if not dev_mode:
		driver.set_window_size(1920, 1080)
	else:
		driver.maximize_window()
	return driver


def create_chrome_driver_wired(dev_mode=False):
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	if not dev_mode:
		options.add_argument('--headless')
	driver = wiredriver.Chrome(options=options)
	if not dev_mode:
		driver.set_window_size(1920, 1080)
	else:
		driver.maximize_window()
	return driver
