from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SWIMLANE_ORDER = {"HOTEL":1, 
                      "FORFAIT":2, 
                      "CLASES":3, 
                      "ACTIVIDADES":4,
                      "ALQUILER":5,
                      "RESTAURACION":6}

    SELECIONAR_FORFAIT = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["FORFAIT"]}]/label/div[1]')
    SELECCIONAR_CLASES = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["CLASES"]}]/label/div[1]')
    SELECCIONAR_ACTIVIDADES = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["ACTIVIDADES"]}]/label/div[1]')
    SELECCIONAR_HOTEL = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["HOTEL"]}]/label/div[1]')
    SELECCIONAR_ALQUILER = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["ALQUILER"]}]/label/div[1]')
    SELECCIONAR_RESTAURACION = (By.XPATH, f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{SWIMLANE_ORDER["RESTAURACION"]}]/label/div[1]')

    COOKIE_BUTTON = (By.ID, "CybotCookiebotDialogBodyButtonAccept")
    SWIMLANES = (By.CSS_SELECTOR, "[class='btnb-list-checkbox__unrelated  ']")
    CONTINUAR = (By.ID, "edit-submit")

    def swimlane_name(interator):
        ...
        name = f'//*[@id="bntb-list-checkbox"]/div/div/div/div[{interator}]/label/div[2]/div/div[2]/div/div'
        return name

class CalendarPageLocators(object):
    
    
    def day_cs_selector(timestamp):

        css_selector = f"[data-time='{timestamp}']"
        return css_selector

    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "button-next-month")

class ClasesPageLocators(object):

    CLASE_COLECTIVA = (By.XPATH, f'//*[@id="edit-step-container"]/div[3]/label/div[2')
    
    '//*[@id="edit-step-container"]/div[3]/label/div[2]'
    '//*[@id="edit-step-container"]/div[4]/label/div[2]'