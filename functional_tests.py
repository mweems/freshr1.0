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

	def test_can_get_to_feed_page_from_home_page(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Freshr', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Freshr', header_text)

		sell_button = self.browser.find_element_by_id('sell_fish')
		buy_button = self.browser.find_element_by_id('buy_fish')

		buy_button.send_keys(Keys.ENTER)

		feed_post_url = self.browser.current_url
		self.assertRegex(feed_post_url, '/newsFeed/feed')

	def test_submitting_redirects_to_feed_page(self):
		self.browser.get('http://localhost:8000/newsFeed/create')
		self.assertIn('Freshr Create Post', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Create new post', header_text)

		nameInput = self.browser.find_element_by_id('name_input')
		phoneInput = self.browser.find_element_by_id('phone_input')
		inputBox = self.browser.find_element_by_id('text_input')
		submit = self.browser.find_element_by_id('submit')

		self.assertEqual(nameInput.get_attribute('placeholder'), 'Your Name')
		self.assertEqual(phoneInput.get_attribute('placeholder'), 'Your Phone Number')
		self.assertEqual(inputBox.get_attribute('placeholder'), 'What you are selling')

		submit.click()

		feed_post_url = self.browser.current_url
		self.assertRegex(feed_post_url, '/newsFeed/feed')

	def test_can_save_post_and_read_it_later(self):
		self.browser.get('http://localhost:8000/newsFeed/create')

		nameInput = self.browser.find_element_by_id('name_input')
		phoneInput = self.browser.find_element_by_id('phone_input')
		inputBox = self.browser.find_element_by_id('text_input')
		submit = self.browser.find_element_by_id('submit')

		nameInput.send_keys('Matt')
		phoneInput.send_keys('808-420-6969')
		inputBox.send_keys('10lbs Tuna, $5 per lb')

		submit.click()

		table = self.browser.find_element_by_id('feed_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn('Matt', [row.text for row in rows])
		self.assertIn('808-420-6969', [row.text for row in rows])
		self.assertIn('10lbs Tuna, $5 per lb', [row.text for row in rows])


if __name__== '__main__':
	unittest.main(warnings='ignore')