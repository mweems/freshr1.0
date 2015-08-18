from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewFishermanTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_get_to_create_post_page_from_home_page(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Freshr', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Freshr', header_text)

		sell_button = self.browser.find_element_by_id('sell_fish')
		buy_button = self.browser.find_element_by_id('buy_fish')

		sell_button.send_keys(Keys.ENTER)

		create_post_url = self.browser.current_url
		self.assertRegex(create_post_url, '/newsFeed/create')


if __name__== '__main__':
	unittest.main(warnings='ignore')