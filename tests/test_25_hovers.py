from utils.create_driver import create_chrome_driver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestHovers:
	def setup_method(self):
		self.driver = create_chrome_driver(dev_mode=False)
		self.driver.get('http://localhost:7080/hovers')

	def teardown_method(self):
		self.driver.quit()

	def hover_over(self, elem: WebElement):
		ActionChains(self.driver).move_to_element(elem).perform()

	def test_hovers(self):
		imgs = WebDriverWait(self.driver, 5).until(
			EC.visibility_of_all_elements_located(
				(By.XPATH, '//img[@alt="User Avatar"]')
			)
		)
		captions = WebDriverWait(self.driver, 5).until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, 'figcaption'))
		)
		for i in range(len(imgs)):
			ActionChains(self.driver).move_to_element(imgs[i]).perform()
			for j in range(len(captions)):
				caption = captions[j]
				assert caption.find_element(
					By.TAG_NAME, 'h5'
				).is_displayed() == (i == j)
				assert caption.find_element(
					By.TAG_NAME, 'a'
				).is_displayed() == (i == j)
