import requests
import pandas
from bs4 import BeautifulSoup
import json
from format_data import format_data

def scraping():
    covid = requests.get('https://news.google.com/covid19/map?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&mid=%2Fm%2F015fr')

    covid = covid.content

    soup = BeautifulSoup(covid, 'html.parser')
    table_covid = str(soup.find(name='table'))
    table_covid = pandas.read_html(table_covid)[0]

    data_covid = table_covid[[
        'Local',
        'Total de casos', 
        'Novos casos (1 dia*)', 
        'Casos a cada um milhão de pessoas', 
        'Mortes'
        ]]
    data_covid.columns = ['local', 'casos', 'novos casos', 'casos por milhão', 'mortes']
    data_covid = data_covid.to_dict('records')

    data = json.dumps(format_data(data_covid))
    file = open("../data.json", 'w')
    file.write(data)
    file.close()

scraping()