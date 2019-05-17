from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
from unittest import skip

from .base import FunctionalTest
	
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

@skip
class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Christa goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)
        
        # She starts a new list and sees that the iput is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)

