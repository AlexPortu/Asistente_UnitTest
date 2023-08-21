import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By


class AsistenteSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://assistant.grandvalira.com/assistant/intereses")

    def test_swimlane_forfait(self):


        #Carga la página principal. La que se determine en setUp()
        main_page = page.MainPage(self.driver)

        #Aceptar cookies
        main_page.click_cookie_button()

        #Verifica que existe la swimlane
        servicio = "forfait"
        swimlanes = main_page.buscar_swimlane(servicio)
        self.assertEqual(swimlanes, True)
    
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()