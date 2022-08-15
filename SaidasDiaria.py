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
time.sleep(5)

catalogo = "Abre aí vai...❤️https://docs.google.com/forms/d/1VdpprXoDO8zj15zz-edOoBCSABB7UR6uAjJM56bC-y8/edit"
texto = '''Oiieee 😄

Me chamo Jirlayne, prazer!
Sou responsável pelo cliente Alugue Flat Temporada

Tivemos a hora de te receber em nosso paraíso, e estamos curiosos para saber..
como foi os dias de lazer? contaaa tudo!!👀

➡️ Aqui, seu feedback vale 10% de desconto na próxima viagem

Clique no link para avaliar sua experiência, juro que  é rapidão! ⏰


'''
mouse = Controller()

ji = "Ji Midia Aft" 
contato = ['wa.me/5531975587358',
'wa.me/5517996668683',
'wa.me/556285736448',
'wa.me/5599984824205',
'wa.me/5581991132844',
'wa.me/5563999613038',
'wa.me/5563992838575',
'wa.me/5563999853631',
'wa.me/5531999186113',
'wa.me/5564999336273',
'wa.me/5511986654751',
'wa.me/5562994985960',
'wa.me/5584996139279',
'wa.me/5536984122092',
'wa.me/558197521828',
'wa.me/5569985002384',
'wa.me/5521999359853',
'wa.me/5533988224992',
'wa.me/5567996084415',
'wa.me/5562982794128',
'wa.me/5541991194829',
'wa.me/558185874452',
'wa.me/5581999831081',
'wa.me/556992377676',
'wa.me/5584996294461',
'wa.me/558187817734',
'wa.me/5527981783328',
'wa.me/5548984133580',
'wa.me/5581987006921',
'wa.me/558197065081',
'wa.me/5511974506151',
'wa.me/553191669834',
'wa.me/5511993949242',
'wa.me/553186127588',
'wa.me/558188997749',
'wa.me/5581998538332',
'wa.me/5581997222892',
'wa.me/558188804011',
'wa.me/55995212539',
'wa.me/5561982176094',
'wa.me/5599982660906',
'wa.me/5581996199723',
'wa.me/5582988386212',
'wa.me/5521969301823',
'wa.me/5523162540150',
'wa.me/5581991081469',
'wa.me/5581982370713']

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
    
    
    
    