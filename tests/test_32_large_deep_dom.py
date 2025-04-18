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

# as there is not much to test here, let's figure out the fastest locator strategies
class TestLargeDeepDOMs(BaseTest):
	page_url = '/large'