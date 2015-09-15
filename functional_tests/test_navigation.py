from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time


class NavigationTest(FunctionalTest):
    def test_can_get_to_create_post_page_from_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Freshr', self.browser.title)

        sell_button = self.browser.find_element_by_id('sell_fish')
        sell_button.send_keys(Keys.ENTER)

        create_post_url = self.browser.current_url
        self.assertRegex(create_post_url, '/newsFeed/create')

    def test_can_get_to_feed_page_from_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Freshr', self.browser.title)

        buy_button = self.browser.find_element_by_id('buy_fish')
        buy_button.send_keys(Keys.ENTER)

        feed_post_url = self.browser.current_url
        self.assertRegex(feed_post_url, '/newsFeed/feed')

    def test_submitting_redirects_to_feed_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('sell_fish').send_keys(Keys.ENTER)
        time.sleep(.5)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Create new post', header_text)

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        self.assertEqual(nameInput.get_attribute('placeholder'), 'Your Name')
        self.assertEqual(phoneInput.get_attribute('placeholder'), 'Your Phone Number')
        self.assertEqual(inputBox.get_attribute('placeholder'), 'What you are selling')

        nameInput.send_keys('Matt')
        phoneInput.send_keys('808-420-6969')
        inputBox.send_keys('10lbs Tuna, $5 per lb')

        submit.click()

        feed_post_url = self.browser.current_url
        self.assertRegex(feed_post_url, '/newsFeed/feed')
