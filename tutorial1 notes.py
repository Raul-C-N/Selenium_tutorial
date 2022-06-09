from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\chromedriver_win32\chromedriver.exe"

# Inicia o webdriver e abre a página. Sempre é o primeiro passo
driver = webdriver.Chrome(PATH)

# Abre a página selecionada nos parênteses
driver.get("https://techwithtim.net")
driver.get("https://www.google.com")

# Imprime o título da página
print(driver.title)

#Fecha a aba
driver.close()

#fecha o navegador
driver.quit()

#encontra elemento por id
search = driver.find_element_by_id("input")

#encontra a caixa de busca no site pelo nome 
search = driver.find_element_by_name("")

#insere uma informação
search.send_keys("test")