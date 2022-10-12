from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd 

option = Options()
option.add_argument('--headless') 

conteudo = []
url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='
lista = 0
while lista <=20:
    lista = lista + (1)
    a = str(lista)
    x = url + a
    
    navegar = webdriver.Chrome(options=option)
    navegar.get(x)

    sleep(1.5)

    

    site = BeautifulSoup(navegar.page_source, 'html.parser')


    busca = site.findAll('div', attrs={'class': 'col-sm-4 col-lg-4 col-md-4'})


    for iten in busca:
    

        titulo = iten.find('a', attrs={'class': 'title'})
        preco = iten.find('h4', attrs={'class': 'pull-right price'})
        descricao = iten.find('p', attrs={'class':'description'})


        conteudo.append([titulo.text, preco.text, descricao.text])
    

scrapan = pd.DataFrame(conteudo, columns=[' Computador', ' Preço', ' Descrição'])

scrapan.to_csv('RESULTADO.csv' )