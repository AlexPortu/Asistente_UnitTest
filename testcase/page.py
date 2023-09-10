from element import *
from locator import *
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from selectorvalues import *
from selenium.webdriver.support import expected_conditions as EC

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'keys'

class BasePage(object):
    """ Página base que van a heredar las demás páginas"""
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """ Funciones de la página principal """
    def el_cookie_button(self):
        # Elemento boton aceptar cookies
        element = self.driver.find_element(*MainPageLocators.COOKIE_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        return element

    def el_servicio(self, servicio):
        # Elemento tipo de servicio (forfait, clases, etc...)
        try:
            selectors = SelectorsValues().swimlanes_ids
            selector_id = selectors[servicio]
        except:
            raise ValueError(f"{servicio} no es un valor válido")
        try:
            element = self.driver.find_element(By.XPATH, MainPageLocators.swimlane_xpath_selector(selector_id))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element

        except:
            raise LookupError(f"Elemento '{servicio}' no se encuentra presente")
               
    def el_continuar(self):
        # Elemento boton continuar
        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element

    def el_combinar(self):
        try:
            element = self.driver.find_element(*MainPageLocators.COMBINAR)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element

        except:
            raise LookupError(f"No se encuentra el boton combinar")
        

class CalendarPage(BasePage):
    """Search results page action methods come here"""


    def el_fecha(self, fecha):
        
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        except:
            fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")

        timestamp = datetime.timestamp(fecha_obj)
        timestamp = str(int(timestamp*1000))

        day_element = self.driver.find_element(By.CSS_SELECTOR, CalendarPageLocators.day_cs_selector(timestamp))
        return day_element


    def el_siguiente_mes(self):

        element = self.driver.find_elements(*CalendarPageLocators.NEXT_MONTH_BUTTON)[-1]
        return element

    def cambiar_mes_hasta_encontrar_fecha(self, fecha):
        control = True
        while control:
            try:
                element = self.el_fecha(fecha=fecha)
                element.click()               
                control = False
            
            except:
        
                try:
                    self.el_siguiente_mes().click()

                except:
                    control = False
        time.sleep(1)

    def el_continuar(self):

        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element
    

class SeleccionarClasePage(BasePage):

    def el_producto_clase(self, clase):
        
        try:
            selectors = SelectorsValues().clases_selectors
            selector_clase = selectors[clase]
        except:
            raise ValueError(f"'{clase}' no es un valor válido ")
    
        try:
            element = self.driver.find_element(By.XPATH, ClasesPageLocators.clase_xpath_selector(selector_clase))
            return element
            
        except:
            raise LookupError(f"'{clase}' no se encuentra disponible para esas fechas")
        

    def el_estilo(self, clase, estilo):

        try:
            selectors = SelectorsValues().estilos_selectors
            selector_estilo = selectors[estilo] + SelectorsValues().clases_selectors[clase].split("_")[-1]
        except:
            raise ValueError(f"'{estilo}' no es un valor válido ")
    
        try:
            element = self.driver.find_element(By.ID, selector_estilo)
            return element
            
        except:
            raise LookupError(f"'{clase}' no se encuentra disponible para esas fechas")

    def el_confirmar(self, clase):
        selector_clase = SelectorsValues().clases_selectors[clase].split("_")[-1]
        element = self.driver.find_element(By.XPATH, ClasesPageLocators.confirmar_xpath_selector(selector_clase))
        return element

    def el_continuar(self):
        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element


class SectorPage(BasePage):

    def el_sector(self, sector):
        # Deuvelve el elemento sector
        try:
            selector_sector = SelectorsValues().sectores_selectors[sector]
        except:
            raise ValueError(f"'{sector}' no es un valor válido ")

        try:
            element = self.driver.find_element(By.XPATH, SectorPageLocators.sector_xpath_selector(selector_sector))
            return element
        except:
            raise LookupError(f"{sector} no disponible")
    
    def el_continuar(self):
        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element
    
class UnidadesClasesPage(BasePage):

    def el_añadir_unidades(self):
        
        try:
            element = self.driver.find_element(*UnidadesClasesPageLocators.AÑADIR_UNIDADES)
            return element
        except:
            raise LookupError("No es posible añadir unidades")
    
    def el_nivel(self):
        
        try:
            element = self.driver.find_element(*UnidadesClasesPageLocators.NIVEL)
            return element
        except:
            raise LookupError("No se encuentra el nivel")

    def el_idioma(self):

        try:
            element = self.driver.find_element(*UnidadesClasesPageLocators.IDIOMA)
            return element
        except:
            raise LookupError("No se encuentra el idioma")

    def el_continuar(self):
        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element

class UnidadesForfaitPage(BasePage):

    def el_añadir_unidades(self):   
        try:
            element = self.driver.find_element(*UnidadesForfaitPageLocators.AÑADIR_UNIDADES)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element
        except:
            raise LookupError("No es posible añadir unidades")
    
    def el_continuar(self):

        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element


class AñadirSeguroPage(BasePage):

    def el_seguro(self):

        try:
            element = self.driver.find_element(*AñadirSeguroPageLocators.AÑADIR_SEGURO)
            return element
        except:
            raise LookupError("No es posible añadir el seguro")
    
    def el_nombre(self):
        
        try:
            element = self.driver.find_element(*AñadirSeguroPageLocators.NOMBRE)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element
        except:
            raise LookupError("No es posible añadir el nombre")
        
    def el_apellido(self):
        
        try:
            element = self.driver.find_element(*AñadirSeguroPageLocators.APELLIDO)
            return element
        except:
            raise LookupError("No es posible añadir el apellido")

    def el_confirmar(self):
        try:
            element = self.driver.find_element(*AñadirSeguroPageLocators.CONFIRMAR)
            return element
        except:
            raise LookupError("No es posible confirmar")
        
    def el_continuar(self):
        # Elemento boton continuar
        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        return element


class HotelOpcionesPage(BasePage):

    def el_habitacion(self):

        try:
            element = self.driver.find_element(*HotelesOpcionesPageLocators.HABITACION)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element
        except:
            raise LookupError("No es posible añadir el hotel")

    def el_regimen(self):

        try:
            element = self.driver.find_element(*HotelesOpcionesPageLocators.REGIMEN)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element
        except:
            raise LookupError("No es posible añadir la habitacion")
        
    def el_reservar(self):

        try:
            element = self.driver.find_element(*HotelesOpcionesPageLocators.RESERVAR)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return element
        except:
            raise LookupError("No es posible hacer click en reservar")
    

class HotelForfaitTipoForfait(BasePage):

    def el_continuar(self):

        element = self.driver.find_element(*MainPageLocators.CONTINUAR)
        return element
