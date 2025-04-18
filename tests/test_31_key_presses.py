from utils.base_test import BaseTest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

different_name_mappings = {
	'COMMAND': 'WIN',
	'META': 'WIN',
	'EQUALS': '',
	'HELP': '',
	'NULL': '',
	'RETURN': 'ENTER',
	'SEMICOLON': '',
	'SEPARATOR': 'COMMA',
	'ZENKAKU_HANKAKU': 'WIN_OEM_ENLW',
}


class TestKeyPresses(BaseTest):
	page_url = '/key_presses'

	def get_result_text(self):
		result = self.wait.until(
			EC.visibility_of_element_located((By.ID, 'result'))
		).text[13:]
		return result

	def test_all_keys(self):
		self.wait.until(EC.presence_of_element_located((By.ID, 'result')))
		for key in dir(Keys):
			if not key.startswith('__'):
				ActionChains(self.driver).send_keys(
					getattr(Keys, key)
				).perform()
				result_text = self.get_result_text()
				if key in different_name_mappings.keys():
					assert different_name_mappings[key] == result_text
				else:
					split_key = key.split('_')
					possibilities = [
						key == result_text,
						key == result_text.replace('_', ''),
						split_key[0] == result_text,
					]
					if len(split_key) > 1:
						possibilities.append(split_key[1] == result_text)
					assert any(possibilities)
