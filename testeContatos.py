
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

texto = '''A oportunidade de viajar é agora!😎🌴💦

Conforto, lazer e diversão  nos melhores destinos. 

➡️ Hospedagem até Agosto de 2022, exceto feriados.
➡️ Promoção por tempo limitado
 

Reservas (81) 3203-3432

www.alugueflattemporada.com.br
@alugueflattemporada
'''
mouse = Controller()

ji = "Ji Midia Aft" 
contato = ['Americo Novelli Flores',
'Amiga De Vandilma',
'Amina Roberta',
'Ammanuel Londero',
'Amnada Sayo',
'Amor E Fé',
'Amora',
'Amtour Agencias',
'Amélia',
'Amélia',
'Ana',
'Ana 1 Manawa',
'Ana Amorim',
'Ana Ana',
'Ana Araujo Porto Sol',
'Ana Barros',
'Ana Beatriz',
'Ana Carla',
'Ana Carolina 1',
'Ana Carolina Manawa',
'Ana Carolina 😊',
'Ana Cintia',
'Ana Claudia',
'Ana Claudia',
'Ana Claudia 12',
'Ana Claudia Camargo',
'Ana Cleide',
'Ana Cristina 1',
'Ana Cristina 🌊🏖🏝',
'Ana D’arc',
'Ana Ferraz',
'Ana Flávia - Mãe das Crias',
'Ana Franca',
'Ana Lu',
'Ana Lucia Melo',
'Ana Luiza',
'Ana MaZziero',
'Ana Maria',
'Ana Marina',
'Ana Patrícia',
'Ana Paula',
'Ana Paula (Amiga de alberto Calado)',
'Ana Paula AFT',
'Ana Paula Alves',
'Ana Paula Comercial',
'Ana Paula Flores',
'Ana Paula Hospede Cvc',
'Ana Paula Instagram',
'Ana Paula Nunes',
'Ana Paula Operadora BRT',
'Ana Paula Porto Sol',
'Ana Paula Porto Sol 1',
'Ana Paula ☀️',
'Ana Paula ♡●',
'Ana Paula ❤❤',
'Ana Paulaa',
'Ana Paulaa',
'Ana Paulaaa',
'Ana Porto Sol Flats',
'Ana Priscilla',
'Ana Richene Insta Laguna',
'Ana Santos',
'Ana Silva',
'Ana Valéria',
'Ana Vitoria',
'Ana Xavier',
'Ana almeida',
'Ana ana Campelo',
'Ana lucia',
'Ana maria Araujo Lorega',
'Ana paula Porto Sol 2',
'Ana paula Silva',
'Ana1',
'Anaa',
'Anaa',
'Anaa',
'Anaaa',
'Anaaaa Kelly',
'Anacimandro',
'Anacleto Insta Porto Sol',
'Analeide',
'Analú Santiago',
'Andder Lline',
'Anderlane',
'Anderson',
'Anderson Betolha',
'Anderson Bezerra',
'Anderson Cordeiro',
'Anderson Gomes',
'Anderson Hospede Porto Sol',
'Anderson Lira',
'Anderson silva',
'Anderson---',
'Andre 2 Flores',
'Andre Hublet',
'Andre Marmore',
'Andre Rocha',
'Andrea Cintra',
'Andrea Manawa 4',
'Andrea Pacheco',
'Andrea Santos',
'Andreaa',
'Andreia',
'Andreia Alencar',
'Andreia Flores 2',
'Andreia Flores Do Mar',
'Andreia Grecco',
'Andreia Laguna Beach Flat',
'Andreia Marques',
'Andreia Pereira',
'Andreia mascarini',
'Andreiaa',
'Andreiiaa',
'Andresa',
'Andresa',
'Andresa Ônibus',
'Andressa',
'Andressa Andrade',
'Andressa Araujo',
'Andressa Becker',
'Andressa Ferreira',
'Andressa Ferreira',
'Andressa Goes',
'Andressa Hospede Porto Sol',
'Andrews Silva',
'Andreza Andrade',
'Andreza Andreza',
'Andreza Andreza',
'Andreza Barros',
'Andreza Cristina Barbosa',
'Andreza Luize',
'Andreza Maia',
'Andreza Moreno',
'Andreza Recepção',
'Andreza Teles',
'Andreza santos',
'Andrezaaa',
'Andrielle Freitas',
'Andrrea',
'Andry',
'Andryelle Cavalcante',
'André Albuquerque',
'André Assessor de Davi',
'Andréa',
'Andréa 1',
'Andréia Quadrigêmios',
'Angela',
'Angela Andrade',
'Angela Melo',
'Angelica',
'Angelica Flores Do Mar',
'Angelica Montezuma',
'Angelica Oliveira',
'Angelim M',
'Angelina',
'Anielle',
'Aninha',
'Aninha Silva',
'Anna Hospede Flores',
'Anna Ka',
'Anne',
'Anne Flores do Mar',
'Anny Hiolanda',
'Antonia',
'Antoniel Flores',
'Antonio Drimel',
'Antonio Ferreira',
'Antônia',
'Antônio Dantas',
'Antônio Fábio',
'Antônio Pacheco',
'Any',
'Any Silva',
'Any veras',
'Any1',
'Apolonio Hugo',
'Aquiléa Rocha',
'Aramis',
'Ariadna',
'Ariana Black',
'Ariane',
'Ariane',
'Ariane',
'Ariane 12',
'Ariane Torquato',
'Arianne Polonio',
'Arielly Gisela',
'Arilene',
'Aristides - 971',
'Aristoteles',
'Arlindo',
'Arlison Gomes',
'Armando Laguna',
'Arthur',
'Arthur Costa',
'Aryelle Calixto',
'Asenate Lima',
'Assessora de Patrícia',
'Athana',
'Augusta alves']

#mensagem = ' Ola Tudo bem teste Robo'

def buscar_contato(contato):
    
    
    keyboard.send("Ctrl+n")
    time.sleep(1)
    keyboard.write(contato)
   
    
    time.sleep(2)
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
    time.sleep(2)
    mouse.click(Button.left)
    time.sleep(2)


for contato in contato:
    buscar_contato(contato)
    
    
    
    