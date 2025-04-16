from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestContextMenus(BaseTest):
	page_url = '/context_menu'

	def test_context_menu(self):
		div_box = WebDriverWait(self.driver, 5).until(
			EC.element_to_be_clickable((By.ID, 'hot-spot'))
		)
		action = ActionChains(self.driver)
		action.context_click(div_box).perform()
		assert EC.alert_is_present()
