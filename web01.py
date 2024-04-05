from selenium import webdriver
import selenium
from selenium.webdriver.common import by
from time import sleep
import pandas as pd


class Web:
    def __init__(self):
        self.link = 'https://asloterias.com.br/resultados-da-mega-sena-2023'
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

        jogo = []
        matriz = []
        k = 1
        for i in range(1, 120):
            #print(self.driver.find_element(by.By.XPATH, self.map['concurso']['xpath'].replace('$NUM$', f'{i+3}')).text, end=' ')
            for j in range(1, 7):
                #print(self.driver.find_element(by.By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text, end=' ')
                numero = int(self.driver.find_element(by.By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text)
                jogo.append(numero)
                k += 1
            matriz.append(jogo)
            jogo = []
            #print('')

        for linha in range(len(matriz)):
            for coluna in range(6):
                print(matriz[linha][coluna], end='\t')
            print('')

        planilha = pd.DataFrame(matriz)
        planilha.to_excel('C:/Users/lintelecom/Desktop/mega.xlsx', index=False)

