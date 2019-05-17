from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
from unittest import skip
import time, sys

from .base import FunctionalTest
	
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class ItemValidationTest(FunctionalTest):    
    def test_cannot_add_empty_list_items(self):
        # Christa goes to the home pae and tries to submit an empty list
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        time.sleep(1)        

        # The home page refreshes and there is a an error message saying that the list cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with text and now it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy photo album\n')
        self.check_for_row_in_list_table('1: Buy photo album')

        # She tries to submit an empty message again
        self.browser.find_element_by_id('id_new_item').send_keys('')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Same warning comes
        self.check_for_row_in_list_table('1: Buy photo album')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")


        # She can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Buy another photo album\n')
        self.check_for_row_in_list_table('1: Buy photo album')
        self.check_for_row_in_list_table('2: Buy another photo album')


        self.fail('write me!')

