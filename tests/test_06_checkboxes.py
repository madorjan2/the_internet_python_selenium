from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_ticked(cb):
	return not (cb.get_attribute('checked') is None)


def toggle_cb(cb):
	cb.click()


def tick_cb(cb):
	if not is_ticked(cb):
		cb.click()


def untick_cb(cb):
	if is_ticked(cb):
		cb.click()


class TestCheckboxes:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/checkboxes')

	def teardown_method(self):
		self.driver.quit()

	def test_checkboxes(self):
		form = WebDriverWait(self.driver, 3).until(
			EC.visibility_of_element_located((By.ID, 'checkboxes'))
		)
		cb1, cb2 = form.find_elements(By.TAG_NAME, 'input')
		untick_cb(cb1)
		untick_cb(cb2)
		assert not is_ticked(cb1) and not is_ticked(cb2)
		toggle_cb(cb1)
		assert is_ticked(cb1) and not is_ticked(cb2)
		toggle_cb(cb2)
		assert is_ticked(cb1) and is_ticked(cb2)
		tick_cb(cb1)
		tick_cb(cb2)
		assert is_ticked(cb1) and is_ticked(cb2)
		toggle_cb(cb1)
		assert not is_ticked(cb1) and is_ticked(cb2)
		toggle_cb(cb2)
		assert not is_ticked(cb1) and not is_ticked(cb2)
