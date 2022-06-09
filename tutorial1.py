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

#encontra a caixa de busca no site pelo nome 
search = driver.find_element_by_name("s")
#insere uma informação
search.send_keys("test")
#digita a informação e aperta enter
search.send_keys(Keys.RETURN)

#Fecha o navegador
driver.quit()
