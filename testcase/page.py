from element import BasePageElement
from locator import MainPageLocators
from selenium.webdriver.common.by import By

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'keys'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def click_cookie_button(self):

        element = self.driver.find_element(*MainPageLocators.COOKIE_BUTTON)
        element.click()


    def click_buscar(self):

        element = self.driver.find_element(*MainPageLocators.SELECIONAR_FORFAIT)
        element.click()

    def buscar_swimlane(self, servicio):

        items = self.driver.find_elements(*MainPageLocators.SWIMLINES)
        for num in range(1, len(items)):

            swimline_name = self.driver.find_element(By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{num}]/label/div[2]/div/div[2]/div/div')
            if servicio == swimline_name.text.lower():
                return True
        return False

    
        


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
    
    def find_search_elements(self):

        results = self.driver.find_element(*MainPageLocators.SEARCH_RESULTS)
        return results