from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Se encarga de abrir la pestaña de Chrome en la ubicación seleccionada
driver = webdriver.Chrome()
driver.get("https://assistant.grandvalira.com/assistant/intereses")
time.sleep(5)
print("acabando")
driver.quit()
