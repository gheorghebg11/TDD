from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time
	
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        # Satisfied she goes back to sleep
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,  [row.text for row in rows], "todo item didn't appear in table, text was: \n%s" %table.text)

    def old_test_can_start_a_list_and_retrieve_it_later(self):
	    # Christa heard about a cool new page, she goes and check it out!
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)


	    # She notices the page title and header mention to-do lists
	    #assert 'To-do' in browser.title()
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


	    # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')        


	    # She types "Make photo album" into a text box
        inputbox.send_keys('Make photo album')
	    
        # When she hits enter the page updates she is taken to a new URL and now the page lists "1:Make photo album" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        christa_list_url = self.browser.current_url
        self.assertRegex(christa_list_url, '/lists/.+')


        # There is still a textox inviting her to add another item. She enters "Make another photo album" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make another photo album')

    	# The page updates again and now shows both items on her list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.5)        
        self.check_for_row_in_list_table('1: Make photo album')
        self.check_for_row_in_list_table('2: Make another photo album')

	   
        # Now a new user, Bogdan, comes along to the site
        ## we use a new browser session to make sure that no info is shared through coookies, etc        
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Bogdan visits the homepage, there is no sign of Christa's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Make photo album', page_text)
        
        # Bogdan starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.5)

        # Bogdan gets his own unique UrL
        bogdan_list_url = self.browser.current_url
        self.assertRegex(bogdan_list_url, '/lists/.+')
        self.assertNotEqual(bogdan_list_url, christa_list_url)

        # Again there is no trace of Christa's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Make photo album', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied they both go back to sleep

    
    def test_layout_and_styling(self):
        # Christa goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)
        
        # She starts a new list and sees that the iput is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)



#if __name__ == '__main__':
#    unittest.main() #warnings ='ignore')

