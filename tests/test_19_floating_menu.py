import time

from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class TestFloatingMenu:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.url = 'http://localhost:7080/floating_menu'
		self.driver.get(self.url)

	def teardown_method(self):
		self.driver.quit()

	def are_we_scrolled_down(self):
		menu_style = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'menu'))).get_attribute('style')
		assert float(menu_style[5:-3]) > 0

	def are_elements_visible(self):
		try:
			WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home'))).click()
			assert self.driver.current_url == self.url + '#home'
			WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, 'News'))).click()
			assert self.driver.current_url == self.url + '#news'
			WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact'))).click()
			assert self.driver.current_url == self.url + '#contact'
			WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, 'About'))).click()
			assert self.driver.current_url == self.url + '#about'
		except Exception as e:
			raise AssertionError(e)

	def test_selenium_scroll_by(self):
		ActionChains(self.driver).scroll_by_amount(0, 2000).perform()
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_selenium_scroll_to_element(self):
		a_bottom_of_page = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Elemental Selenium')))
		ActionChains(self.driver).scroll_to_element(a_bottom_of_page).perform()
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_by(self):
		self.driver.execute_script('window.scrollBy(0, 2000)')
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_to(self):
		self.driver.execute_script('window.scrollTo(0, 2000)')
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_javascript_scroll_into_view(self):
		a_bottom_of_page = WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.LINK_TEXT, 'Elemental Selenium')))
		self.driver.execute_script("arguments[0].scrollIntoView()", a_bottom_of_page)
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()

	def test_selenium_keys_pagedown(self):
		body = self.driver.find_element(By.TAG_NAME, 'body')
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.PAGE_DOWN)
		time.sleep(0.5)
		self.are_we_scrolled_down()
		self.are_elements_visible()