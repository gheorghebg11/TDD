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

        # The home page refreshes and there is a an error message saying that the list cannot be blank

        # She tries again with text and now it works

        # She tries to submit an empty message again

        # Same warning comes

        # She can correct it by filling some text in
        self.fail('write me!')

