from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestEntryAd:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/entry_ad')

	def teardown_method(self):
		self.driver.quit()

	def test_entry_ad(self):
		# JS click is needed, because WebElement.click() leads to ElementClickInterceptedException sometimes
		# element click intercepted: Element <p>...</p> is not clickable at point (949, 592). Other element would receive the click: <div class="modal">...</div>
		p_close = WebDriverWait(self.driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//p[text()="Close"]'))
		)
		self.driver.execute_script('arguments[0].click();', p_close)

		WebDriverWait(self.driver, 5).until(
			EC.invisibility_of_element_located((By.ID, 'modal'))
		)
		self.driver.refresh()
		time.sleep(3)
		WebDriverWait(self.driver, 2).until(
			EC.invisibility_of_element_located((By.ID, 'modal'))
		)
		WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.ID, 'restart-ad'))
		).click()
		WebDriverWait(self.driver, 10).until(
			EC.visibility_of_element_located((By.ID, 'modal'))
		)
