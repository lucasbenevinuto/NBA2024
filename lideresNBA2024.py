import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2024_leaders.html'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

lideres_nba = {  'Categoria' : [],
               'Valor na Categoria' : [],
             'Jogador' : [],
             'Time' : []
             }

divs = soup.find_all('div', class_='data_grid_box')

for div in divs:
    corpo = div.find('table', class_ = 'columns')
    div_id = div.find('caption', class_='poptip').text
    lideres_nba['Categoria'].append(div_id)
    primeiro = div
    jogador = primeiro.find('a', href=True).text
    lideres_nba['Jogador'].append(jogador)
    time = primeiro.find('span', class_ = 'desc').text
    lideres_nba['Time'].append(time)
    value = primeiro.find('td', class_="value").text
    lideres_nba['Valor na Categoria'].append(value)

lideres_df = pd.DataFrame(lideres_nba)
print(lideres_df)