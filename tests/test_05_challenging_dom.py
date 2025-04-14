from utils.create_driver import create_chrome_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import base64
import pytesseract
import io
import os
from PIL import Image


def read_expected():
	this_folder_path = os.path.abspath(
		os.path.join(os.path.realpath(__file__), os.pardir)
	)
	path = os.path.join(this_folder_path, 'test_data', 'test_5.csv')
	with open(path, 'r') as testdata_csv:
		csv_reader = csv.reader(testdata_csv)
		testdata_list = list(csv_reader)
	return testdata_list


class TestChallengingDom:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/challenging_dom')

	def teardown_method(self):
		self.driver.quit()

	def get_button1(self):
		return WebDriverWait(self.driver, 3).until(
			EC.element_to_be_clickable((By.XPATH, '//a[@class="button"]'))
		)

	def get_button2(self):
		return WebDriverWait(self.driver, 3).until(
			EC.element_to_be_clickable(
				(By.XPATH, '//a[@class="button alert"]')
			)
		)

	def get_button3(self):
		return WebDriverWait(self.driver, 3).until(
			EC.element_to_be_clickable(
				(By.XPATH, '//a[@class="button success"]')
			)
		)

	def get_table(self):
		return WebDriverWait(self.driver, 3).until(
			(EC.visibility_of_element_located((By.TAG_NAME, 'table')))
		)

	def get_num_from_dom(self):
		scripts = self.driver.find_elements(By.TAG_NAME, 'script')
		for script in scripts:
			if 'Answer: ' in script.get_attribute('innerHTML'):
				return (
					script.get_attribute('innerHTML')
					.split('Answer: ')[1]
					.split("'")[0]
				)
		raise ValueError('No script tag with an answer on page')

	def test_buttons(self):
		for func in [self.get_button1, self.get_button2, self.get_button3]:
			button1_id = self.get_button1().get_attribute('id')
			func().click()
			assert self.get_button1().get_attribute('id') != button1_id

	def test_table(self):
		table_content = []
		ths = self.get_table().find_elements(By.XPATH, '//thead//th')
		table_content.append([th.text for th in ths])
		trs = self.get_table().find_elements(By.XPATH, '//tbody/tr')
		for tr in trs:
			tds = tr.find_elements(By.TAG_NAME, 'td')
			table_content.append([td.text for td in tds])
		assert table_content == read_expected()

	def test_image(self):
		canvas = self.driver.find_element(By.ID, 'canvas')
		img_base64 = self.driver.execute_script(
			"return arguments[0].toDataURL('image/png').substring(21);", canvas
		)
		img_data = Image.open(io.BytesIO(base64.b64decode(img_base64)))
		num = pytesseract.image_to_string(img_data).split(': ')[1].strip()
		assert num == self.get_num_from_dom()
