from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from time import sleep

class Web:
    def __init__(self):
        self.link = 'https://asloterias.com.br/resultados-da-mega-sena-2022?ordenacao=crescente'
        self.map = {
            'numeros': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[$NUM$]'
            },
            'concurso': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[$NUM$]'
            }
        }

        self.driver = webdriver.Edge()

    def abrir_site(self):
        self.driver.get(self.link)
        sleep(2)

        k = 0
        for i in range(1, 111):
            print(self.driver.find_element(By.XPATH, self.map['concurso']['xpath'].replace('$NUM$', f'{i+3}')).text, end=' ')
            for j in range(6):
                k += 1
                print(self.driver.find_element(By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text, end=' ')
            print('')