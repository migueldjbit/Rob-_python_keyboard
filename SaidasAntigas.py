from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import keyboard
from pynput.mouse import Button, Controller



#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://web.whatsapp.com/')
time.sleep(5)

catalogo = "https://wa.me/c/558187553432"
texto = '''Oiieee 😄

Me chamo Jirlayne, prazer!
Sou responsável pelo cliente Alugue Flat Temporada
Tivemos a hora de te receber em nosso paraíso,*Pousada Flores do Mar* em Porto de Galinhas. Lembra ?
 Estamos com uma promoção imperdível para você e o melhor com 10% de desconto.
Para o mês de Maio.
Confira nosso catalogo.


'''
mouse = Controller()

ji = "Ji Midia Aft" 
contato = ['wa.me/5581996972537']


#mensagem = ' Ola Tudo bem teste Robo'

def buscar_contato(contato):
    #campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    keyboard.send("Ctrl+n")
    time.sleep(1)
    keyboard.write("ji Midia")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(2)
    keyboard.write(contato)
    time.sleep(2)
    keyboard.send("enter")
    time.sleep(8)
    mouse.position = (578, 720)
    mouse.click(Button.left)
    time.sleep(4)
    keyboard.write(texto)
    time.sleep(4)
    keyboard.write(catalogo)
    time.sleep(4)
    keyboard.send("enter")
    time.sleep(2)
    
    
    
    #time.sleep(4)
   # campo_pesquisa.click()
    #campo_pesquisa.send_keys(contato)
    #campo_pesquisa.send_keys(Keys.ENTER)
    #time.sleep(2)
   # keyboard.send("Ctrl+v")
    #keyboard.send("enter")


#def enviar_mensagem(mensagem):
 #   campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
  #  campo_mensagem[1].click()
   # time.sleep(3)
    #campo_mensagem[1].click()
    #campo_mensagem[1].send_keys(mensagem)
    #campo_mensagem[1].send_keys(Keys.ENTER)


    
for contato in contato:
    buscar_contato(contato)
    
    #enviar_mensagem(mensagem)
    
    
    
    