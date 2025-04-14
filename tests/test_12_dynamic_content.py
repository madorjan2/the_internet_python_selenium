from utils.create_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDynamicContent:
	def setup_method(self):
		self.driver = create_chrome_driver()
		self.driver.get('http://localhost:7080/dynamic_content')

	def teardown_method(self):
		self.driver.quit()

	def are_different(self, str_list):
		zeroths = [str_list[i][0] for i in range(len(str_list))]
		firsts = [str_list[i][1] for i in range(len(str_list))]
		seconds = [str_list[i][2] for i in range(len(str_list))]
		return (
			len(set(zeroths)) > 1
			and len(set(firsts)) > 1
			and len(set(seconds)) > 1
		)

	def test_dynamic_content(self):
		profile_pics = []
		descriptions = []
		for i in range(10):
			current_pics = WebDriverWait(self.driver, 2).until(
				EC.visibility_of_all_elements_located(
					(By.XPATH, '//div[@id="content"]//img')
				)
			)
			profile_pics.append(
				[element.get_attribute('src') for element in current_pics]
			)
			current_desc = WebDriverWait(self.driver, 2).until(
				EC.visibility_of_all_elements_located(
					(
						By.XPATH,
						'//div[@id="content"]//div[@class="large-10 columns"]',
					)
				)
			)
			descriptions.append([element.text for element in current_desc])
			self.driver.refresh()
		assert self.are_different(profile_pics) and self.are_different(
			descriptions
		)
