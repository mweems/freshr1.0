from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time


class CreatePostTest(FunctionalTest):

    def test_can_create_a_post(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('sell_fish').send_keys(Keys.ENTER)
        time.sleep(.5)

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        nameInput.send_keys('Matt')
        phoneInput.send_keys('808-420-6969')
        inputBox.send_keys('10lbs Tuna, $5 per lb')

        submit.click()

        post = self.browser.find_element_by_id('post')

        self.assertIn('Matt', post.text)
        self.assertIn('808-420-6969', post.text)
        self.assertIn('10lbs Tuna, $5 per lb', post.text)

    def test_can_go_back_to_create_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('sell_fish').send_keys(Keys.ENTER)
        time.sleep(.5)

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        nameInput.send_keys('Matt')
        phoneInput.send_keys('808-420-6969')
        inputBox.send_keys('10lbs Tuna, $5 per lb')

        submit.click()

        self.browser.find_element_by_id('create_post').click()

        create_post_url = self.browser.current_url
        self.assertRegex(create_post_url, '/newsFeed/create')

    def test_can_add_multiple_posts(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('sell_fish').send_keys(Keys.ENTER)
        time.sleep(.5)

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        nameInput.send_keys('Matt')
        phoneInput.send_keys('808-420-6969')
        inputBox.send_keys('10lbs Tuna, $5 per lb')

        submit.click()

        self.browser.find_element_by_id('create_post').click()

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        nameInput.send_keys('Paula')
        phoneInput.send_keys('808-421-6970')
        inputBox.send_keys('20lbs Ahi, $5 per lb')

        submit.click()

        post = self.browser.find_element_by_id('post')

        self.assertIn('Matt', post.text)
        self.assertIn('808-420-6969', post.text)
        self.assertIn('10lbs Tuna, $5 per lb', post.text)

        self.assertIn('Paula', post.text)
        self.assertIn('808-421-6970', post.text)
        self.assertIn('20lbs Ahi, $5 per lb', post.text)
