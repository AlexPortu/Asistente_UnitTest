import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By
import time

class AsistenteSearch(unittest.TestCase):


    def setUp(self):
       
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://assistant.grandvalira.com/assistant/intereses')


    def test_swimlane_colectivas(self):
        """ Va a testear una swimlane entera de Clases. 
        Es necesario dar como input los siguientes valores"""

        # Para saber que inputs son posibles consultar selectorvalues.py en el mismo directorio. Las claves son los inputs posibles por el usuario
        swimlane = "clases"
        fecha_entrada = "02/12/2023"  # FORMATO: DIA/MES/AÑO
        fecha_salida = "03/12/2023"  # FORMATO: DIA/MES/AÑO
        tipo_clase = "colectivas"
        estilo = "esqui"
        sector = "tarter"

        # Carga la página principal. La que se determine en setUp()
        main_page = page.MainPage(self.driver)
        # Aceptar cookies
        main_page.el_cookie_button().click()
        # hacer click en la swinlane
        self.driver.execute_script("arguments[0].scrollIntoView()", main_page.el_servicio(swimlane))
        main_page.el_servicio(swimlane).click()
        main_page.el_continuar().click()
        
        calendar_page = page.CalendarPage(self.driver)
        # Busca y hace click en la fecha de entrada
        calendar_page.cambiar_mes_hasta_encontrar_fecha(fecha_entrada)
        # Busca y hace click en la fecha de salida
        calendar_page.el_fecha(fecha_salida).click()
        calendar_page.el_continuar().click()
        time.sleep(0.5)

        clases_page = page.SeleccionarClasePage(self.driver)
        # Busca que la clase seleccionada esté disponible para esas fechas y la selecciona
        try:
            clases_page.el_producto_clase(tipo_clase).click()
        except Exception as err:
            assert False
        time.sleep(0.5)
        clases_page.el_estilo(tipo_clase, estilo).click()
        clases_page.el_confirmar(tipo_clase).click()
        clases_page.el_continuar().click()
        time.sleep(1)

        sector_page = page.SectorPage(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView()", sector_page.el_sector(sector))
        sector_page.el_sector(sector).click()
        sector_page.el_continuar().click()
        time.sleep(1)
        
        unidades_page = page.UnidadesClasesPage(self.driver)
        unidades_page.el_añadir_unidades().click() # Hace click una vez en el primer boton. Falta configurar añadir multiples unidades.
        unidades_page.el_nivel().click()
        unidades_page.el_idioma().click()
        unidades_page.el_continuar().click()
        time.sleep(2)
        assert True


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
