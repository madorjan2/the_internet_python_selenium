from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestDragAndDrop(BaseTest):
	page_url = '/drag_and_drop'

	def test_drag_and_drop(self):
		left_box = WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.ID, 'column-a'))
		)
		right_box = WebDriverWait(self.driver, 2).until(
			EC.element_to_be_clickable((By.ID, 'column-b'))
		)
		assert left_box.text == 'A' and right_box.text == 'B'
		ActionChains(self.driver).drag_and_drop(left_box, right_box).perform()
		assert left_box.text == 'B' and right_box.text == 'A'
		ActionChains(self.driver).drag_and_drop(left_box, right_box).perform()
		assert left_box.text == 'A' and right_box.text == 'B'
