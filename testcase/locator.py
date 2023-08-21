from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'edit-submit')
    COOKIE_BUTTON = (By.ID, "CybotCookiebotDialogBodyButtonAccept")
    SWIMLINES = (By.CSS_SELECTOR, "[class='btnb-list-checkbox__unrelated  ']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass