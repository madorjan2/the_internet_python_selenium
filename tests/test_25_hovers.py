from utils.base_test import BaseTest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestHovers(BaseTest):
	page_url = '/hovers'

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
