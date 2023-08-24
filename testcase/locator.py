from selenium.webdriver.common.by import By

class MainPageLocators(object):

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


class CalendarPageLocators(object):
    
    def day_cs_selector(timestamp):

        css_selector = f"[data-time='{timestamp}']"
        return css_selector

    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "button-next-month")


class ClasesPageLocators(object):

    def clase_css_selector(clase):
        # Valor dentro del atributo "for" del div
        clases_selectors = {"colectivas": "clase_209", "particulares": "clase_237"}
        return "#edit-step-container > div:nth-child(3)"
        return f"[for='{clases_selectors[clase]}'] > [class='btnb-list-checkbox__ch-img-cont combined-child']"