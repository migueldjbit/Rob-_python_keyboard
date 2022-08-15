from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path=r'C:\Users\djmig\Desktop\Python\geckodriver.exe')
from selenium.webdriver.common.keys import Keys

driver.get('https://web.whatsapp.com/')


time.sleep(20)


contato = ['Junior Tati Tm','Ingrid']
mensagem = 'Olá tudo bem teste de Robo '

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].click()
    
   
    
for contato in contato:
    buscar_contato(contato)
    enviar_mensagem(mensagem)