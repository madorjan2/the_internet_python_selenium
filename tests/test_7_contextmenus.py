from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestContextMenus:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/context_menu')

	def teardown_method(self):
		self.driver.quit()

	def test_context_menu(self):
		div_box = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'hot-spot')))
		action = ActionChains(self.driver)
		action.context_click(div_box).perform()
		assert EC.alert_is_present()

