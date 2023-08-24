from element import *
from locator import *
from selenium.webdriver.common.by import By
from datetime import datetime
import time


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


    def click_cookie_button(self):

        element = self.driver.find_element(*MainPageLocators.COOKIE_BUTTON)
        element.click()


    def seleccionar_servicio(self, servicio):

        servicios = {
            "forfait": self.driver.find_element(*MainPageLocators.SELECIONAR_FORFAIT),
            "hotel": self.driver.find_element(*MainPageLocators.SELECCIONAR_HOTEL),
            "clases": self.driver.find_element(*MainPageLocators.SELECCIONAR_CLASES),
            "alquiler": self.driver.find_element(*MainPageLocators.SELECCIONAR_ALQUILER),
            "restauracion": self.driver.find_element(*MainPageLocators.SELECCIONAR_RESTAURACION),
            "actividades": self.driver.find_element(*MainPageLocators.SELECCIONAR_ACTIVIDADES)
        }
        
        element = servicios[servicio]
        
        return element


    def continuar(self):

        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element

"""    def buscar_swimlane(self, servicio):

        items = self.driver.find_elements(*MainPageLocators.SWIMLANES)
        for num in range(1, len(items)):

            swimline_name = self.driver.find_element(By.XPATH, MainPageLocators.swimlane_name(num))
            if servicio == swimline_name.text.lower():
                return True
        return False"""   
        

class CalendarPage(BasePage):
    """Search results page action methods come here"""


    def encontrar_fecha(self, fecha):
        
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        except:
            fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")

        timestamp = datetime.timestamp(fecha_obj)
        timestamp = str(int(timestamp*1000))

        day_element = self.driver.find_element(By.CSS_SELECTOR, CalendarPageLocators.day_cs_selector(timestamp))
        return day_element


    def siguiente_mes(self):

        element = self.driver.find_elements(*CalendarPageLocators.NEXT_MONTH_BUTTON)[-1]
        return element

    def cambiar_mes_hasta_encontrar_fecha(self, fecha):
        control = True
        while control:
            time.sleep(0.5)
            try:
                element = self.encontrar_fecha(fecha=fecha)
                element.click()               
                control = False
            
            except:
        
                try:
                    self.siguiente_mes().click()

                except:
                    control = False

                time.sleep(0.5)
        time.sleep(2)

    def click_continuar(self):

        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        element.click()
    

class SeleccionarClasePage(BasePage):

    def encontrar_clase(self, clase):
        
        element = self.driver.find_element(By.CSS_SELECTOR, ClasesPageLocators.clase_css_selector(clase))
        return element