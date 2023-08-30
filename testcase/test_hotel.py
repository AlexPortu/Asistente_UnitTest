import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class AsistenteSearch(unittest.TestCase):


    def setUp(self):
       
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        # to supress the error messages/logs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.start_url = 'https://assistant.grandvalira.com/assistant/intereses'
        self.driver.get(self.start_url)


    def test_swimlane_hotel(self):
        """ Va a testear una swimlane entera de Hotel. 
        Es necesario dar como input los siguientes valores"""
        # Para saber que inputs son posibles consultar selectorvalues.py en el mismo directorio. Las claves son los inputs posibles por el usuario
        swimlane = "forfait"
        fecha_entrada = "02/12/2023"  # FORMATO: DIA/MES/AÑO
        fecha_salida = "03/12/2023"  # FORMATO: DIA/MES/AÑO     
        adultos = 1
        seguro = True

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

        unidades_page = page.UnidadesForfaitPage(self.driver)
        unidades_page.el_añadir_unidades().click()
        unidades_page.el_continuar().click()

        time.sleep(0.5)

        seguro_page = page.AñadirSeguroPage(self.driver)
        seguro_page.el_seguro().click()
        
        seguro_page.el_nombre().send_keys("Test")
        seguro_page.el_apellido().send_keys("Test")
        seguro_page.el_confirmar().click()
        seguro_page.el_continuar().click()
        
        # Comprueba que hemos llegado al final del camino cotejando la url inicial con la final. La web debería derivar a self.start_url al acabar la swimlane
        if self.start_url == self.driver.current_url: assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
