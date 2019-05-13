from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
	
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        # Satisfied she goes back to sleep
        self.browser.quit()

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

	    # She types "Make photo album Luca" into a text box
        inputbox.send_keys('Buy photo album')

	    # When she hits enter the page updates and now the page lists "1:Make photo album Luca" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy photo album' for row in rows), "todo item didn't appear in table")

	    # There is still a textox inviting her to add another item. She enters "Make another photo album" 
        self.fail('Finish the test!')

	# The page updates again and now shows both items on her list



	# Christa wonders wheter the site will rememer her list. The she sees that the site has generated a unique URL for her


	# She visits that URL - the to-do list is still there!

if __name__ == '__main__':
    unittest.main() #warnings ='ignore')

