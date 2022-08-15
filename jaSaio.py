from email.mime import image
from tkinter import PhotoImage, image_names, image_types
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import keyboard
from pynput.mouse import Button, Controller


#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://web.whatsapp.com/')
time.sleep(2)

texto = '''Segue o Comprovante da Albertina Pereira
pago no prazo ja informado ao 
Maria Martins 
Victor Pinheiro 
Cristiane Chacarosque
Tatiele de Sá 
ingrid
'''
mouse = Controller()

ji = "Ji Midia Aft" 
contato = ['11996397100',
'11996451674',
'11996555491',
'11996590244',
'11996959529',
'11997478724',
'11997798004',
'11997806333',
'11997913107',
'11998106672']

#mensagem = ' Ola Tudo bem teste Robo'

def buscar_contato(contato):
    
    
    keyboard.send("Ctrl+n")
    time.sleep(1)
    keyboard.write(contato)
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(2)
    keyboard.write(texto)
    time.sleep(2)
    keyboard.send("enter")      
    time.sleep(2)
    mouse.position = (384, 795)
    mouse.click(Button.left)
    time.sleep(1)
    mouse.position = (382, 748)
    mouse.click(Button.left)
    time.sleep(1)
    mouse.position = (562, 225)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.send("Ctrl+a")
    time.sleep(1)
    keyboard.send("enter")
    time.sleep(3)
    mouse.position = (750, 778)
    mouse.click(Button.left)
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
    
    
    
    