from selenium.webdriver.common.by import By

""" Parametros de la 'funcion find_element' donde establece el tipo de búsqueda y sus localización en el html """
class MainPageLocators(object):
    """ Localizadores de la página principal """

    #Swimlanes --> Localiza el id dentro del div. Para añadir valores copiar xpath y cambiar @id=xxxx
    def swimlane_xpath_selector(swimlane):
        return f"//*[@id={swimlane}]//ancestor::div[contains(@class, 'btnb-list-checkbox__unrelated  ')]"
    
    COOKIE_BUTTON = (By.ID, "CybotCookiebotDialogBodyButtonAccept")
    CONTINUAR = (By.ID, "edit-submit")


class CalendarPageLocators(object):
    """ Localizadores de la página de Calendario """
    
    def day_cs_selector(timestamp):
        #Encuentra el elemento en el HTML dependiendo de la fecha que pide el usuario del test
        css_selector = f"[data-time='{timestamp}']"
        return css_selector

    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "button-next-month")


class ClasesPageLocators(object):
    """ Localizadores de la página de selección de clases """

    def clase_xpath_selector(clase):
        #Encuentra el elemento según el input del usuario. Se mantiene en SelectorValues() los valores posibles
        return f"//label[@for='{clase}']//ancestor::div[contains(@class, 'btnb-list-checkbox__unrelated')]"
    
    def confirmar_xpath_selector(clase):
        return f"//*[@id='btnb-plusinput_{clase}']//child::div[contains(@class, 'btnb-popup__continue')]"

class SectorPageLocators(object):
    """ Localizadores de la página de selección de sector """

    def sector_xpath_selector(sector):
        # Encuentra el sector según el input. Posibles inputs en SectorValues()
        return f"//*[@id='sector_L{sector}']//ancestor::div[contains(@class, 'btnb-list-checkbox__unrelated  ')]"

class UnidadesClasesPageLocators(object):
    """ Localizadores de la página de selección de unidades de clases"""

    AÑADIR_UNIDADES = (By.XPATH, "//*[@class='cl_options__button b_add']")
    NIVEL = (By.XPATH, "//select[contains(@name, 'nivel_45673_c_')]/option[text()='Debutante']")
    IDIOMA = (By.XPATH, "//select[contains(@name, 'idioma_45673_c_')]/option[text()='Español']")

class UnidadesForfaitPageLocators(object):
    """ Localizadores de la página de selección de unidades de forfait"""

    AÑADIR_UNIDADES = (By.XPATH, "//*[contains(@class, 'has-icon plus')]")

class AñadirSeguroPageLocators(object):
    """ Localizadores de la página de añadir seguro """

    AÑADIR_SEGURO = (By.XPATH, "//div[contains(@class, 'wrapper btnb-add-insurance js-form-wrapper form-wrapper')]")
    NOMBRE = (By.XPATH, "//*[@id='edit-insurance-name-1']")
    APELLIDO = (By.XPATH, "//*[@id='edit-insurance-surname-1']")
    CONFIRMAR = (By.XPATH, "//div[contains(@id, 'edit-btnb-container')]//child::div[contains(@class, 'btnb-popup__confirmation btnb-popup__index-1')]")


