from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SELECIONAR_FORFAIT = (By.ID, 'interes2')
    SELECCIONAR_CLASES = (By.ID, 'interes2')
    SELECCIONAR_ACTIVIDADES = (By.ID, 'interes2')
    SELECCIONAR_HOTEL = (By.ID, 'interes2')
    SELECCIONAR_ALQUILER = (By.ID, 'interes2')
    SELECCIONAR_RESTAURACION = (By.ID, 'interes2')

    COOKIE_BUTTON = (By.ID, "CybotCookiebotDialogBodyButtonAccept")
    SWIMLINES = (By.CSS_SELECTOR, "[class='btnb-list-checkbox__unrelated  ']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass