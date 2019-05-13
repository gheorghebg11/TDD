from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Satisfied she goes back to sleep
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
	# Christa heard about a cool new page, she goes and check it out!
        self.browser.get('http://localhost:8000')

	# She notices the page title and header mention to-do lists
	#assert 'To-do' in browser.title()
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')

	# She is invited to enter a to-do item straight away

	# She types "Make photo album Luca" into a text box


	# When she hits enter the page updates and now the page lists "1:Make photo album Luca" as an item in a to-do list


	# There is still a textox inviting her to add another item. She enters "Make another photo album" 


	# The page updates again and now shows both items on her list



	# Christa wonders wheter the site will rememer her list. The she sees that the site has generated a unique URL for her


	# She visits that URL - the to-do list is still there!

if __name__ == '__main__':
    unittest.main() #warnings ='ignore')

