from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time
	
class NewVisitorTest(unittest.TestCase):

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


    def test_can_start_a_list_and_retrieve_it_later(self):
	    # Christa heard about a cool new page, she goes and check it out!
        self.browser.get('http://localhost:8000')


	    # She notices the page title and header mention to-do lists
	    #assert 'To-do' in browser.title()
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


	    # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')        


	    # She types "Buy photo album" into a text box
        inputbox.send_keys('Make photo album')
	    
        # When she hits enter the page updates and now the page lists "1:Make photo album" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Make photo album')


        # She types "Make another photo album" into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make another photo album')

	    # When she hits enter the page updates and now the page lists "1:Make another photo album" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        check_for_row_in_list_table(self, '2: Make another photo album')


	    # There is still a textox inviting her to add another item. She enters "Make another photo album" 
        self.fail('Finish the test!')

    	# The page updates again and now shows both items on her list



	    # Christa wonders wheter the site will rememer her list. The she sees that the site has generated a unique URL for her


    	# She visits that URL - the to-do list is still there!

if __name__ == '__main__':
    unittest.main() #warnings ='ignore')

