from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time


class PostValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('sell_fish').send_keys(Keys.ENTER)
        time.sleep(.5)

        nameInput = self.browser.find_element_by_id('name_input')
        phoneInput = self.browser.find_element_by_id('phone_input')
        inputBox = self.browser.find_element_by_id('text_input')
        submit = self.browser.find_element_by_id('submit')

        submit.click()

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can not leave the name field blank")

        nameInput.send_keys('Matt')
        submit.click()

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can not leave the phone field blank")

        phoneInput.send_keys('808-420-6969')
        submit.click()

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can not leave the text field blank")

        inputBox.send_keys('10lbs Tuna, $5 per lb')
        submit.click()

        post = self.browser.find_element_by_id('post')

        self.assertIn('Matt', post.text)
        self.assertIn('808-420-6969', post.text)
        self.assertIn('10lbs Tuna, $5 per lb', post.text)
