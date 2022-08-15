from selenium import webdriver
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class whatsappboot:

    def _init(self):
        self.mensagem =  '''
Olá , tudo bem?
Me chamo Miguel, prazer!
Sou responsável pela experiência com o cliente da Alugue Flat Temporada.
Recentemente tivemos a honra de lhe receber e gostaríamos de saber o seu nível de satisfação com nossos serviços.

*Poderia responder esse rápido e simples questionário?*
https://docs.google.com/forms/d/1VdpprXoDO8zj15zz-edOoBCSABB7UR6uAjJM56bC-y8/edit

Sua opinião é muito importante para nós!

Queremos te receber mais vezes, então, não deixe de salvar o nosso contato para receber nossas promoções! 😎 🌴

'''
    self.contato["jiji Silva, Vitoria Rocha!"]
    options = webdriver.chromeOptions()
    options.add_argument('lang=pt-br')
    self.drive = webdriver.chrome(executable_path=r'./chromedriver.exe')
    
    def enviarMensagens(self):
    telefone = self.driver.find_element_by_xpath("//span[@title='jiji Silva, Vitoria Rocha!']")
    
    for telefone in self.telefone:
        grupo = self.driver.find_element_by_xpath("//span[@title='jiji Silva, Vitoria Rocha!']")