import pytest

from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestExitIntent(BaseTest):
	page_url = '/exit_intent'

	@pytest.mark.flaky(reruns=3)
	def test_exit_intent(self):
		# I have not found a way to simulate moving the cursor outside the browser window in headless mode
		# therefore I am triggering the event directly
		self.driver.execute_script('_ouibounce.fire()')
		self.wait.until(
			EC.element_to_be_clickable(
				(By.XPATH, '//div[@class="modal-footer"]/p')
			)
		).click()
		self.wait.until(
			EC.invisibility_of_element_located(
				(By.XPATH, '//div[@class="modal-footer"]/p')
			)
		)
