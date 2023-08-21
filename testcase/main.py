import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By


class AsistenteSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://assistant.grandvalira.com/assistant/intereses")

    def test_load_swimlanes(self):


        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "clases"
        main_page.click_cookie_button()

        #Verifies that the results page is not empty
        swimlanes = main_page.read_swimlanes()
        
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()