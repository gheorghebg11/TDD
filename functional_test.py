from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

# She notices the page title and header mention to-do lists
#assert 'To-do' in browser.title()

# She is invited to enter a to-do item straight away


# She types "Make photo album Luca" into a text box


# When she hits enter the page updates and now the page lists "1:Make photo album Luca" as an item in a to-do list


# There is still a textox inviting her to add another item. She enters "Make another photo album" 


# The page updates again and now shows both items on her list


# Christa wonders wheter the site will rememer her list. The she sees that the site has generated a unique URL for her


# She visits that URL - the to-do list is still there!


# Satisfied she goes back to sleep
# browser.quit()
