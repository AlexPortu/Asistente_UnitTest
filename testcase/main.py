import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


class AsistenteSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.set_window_size(1080,1200)
        self.driver.get("https://assistant.grandvalira.com/assistant/intereses")
        

    def test_swimlane_forfait(self):

        #Carga la página principal. La que se determine en setUp()
        main_page = page.MainPage(self.driver)
        action = ActionChains(self.driver)

        #Aceptar cookies
        main_page.click_cookie_button()

        # hacer click en la swinlane
        # click_seleccionar_servicio tiene los siguientes parametros:
        # forfait, clases, hotel, actividades, alquiler, restauracion
        self.driver.execute_script("arguments[0].scrollIntoView()", main_page.seleccionar_servicio("alquiler"))
        time.sleep(0.5)
        main_page.seleccionar_servicio("clases").click()
        main_page.continuar().click()
        

        calendar_page = page.CalendarPage(self.driver)
        # formato fecha --> dia / mes / año. 02/12/2023
        # Busca y hace click en la fecha de entrada
        calendar_page.cambiar_mes_hasta_encontrar_fecha("01/12/2023")
        # Busca y hace click en la fecha de salida
        calendar_page.encontrar_fecha("03/12/2023").click()
        calendar_page.click_continuar()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
