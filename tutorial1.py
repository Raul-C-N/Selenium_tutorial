from webbrowser import Chrome
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\chromedriver_win32\chromedriver.exe"

# Inicia o webdriver e abre a página. Sempre é o primeiro passo
driver = webdriver.Chrome(PATH)

# Abre a página selecionada nos parênteses
driver.get("https://techwithtim.net")

#imprime título da página
print(driver.title)

search = driver.find_element_by_name("s")

#Fecha o navegador
driver.quit()
