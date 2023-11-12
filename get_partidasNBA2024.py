import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/boxscores/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


div = soup.find('div', class_='game_summaries')

jogos = div.find_all('div', class_='game_summary expanded nohover')
dia = soup.find('span', class_ = 'button2 index').text

jogos_nba = {  'Vencedores' : [],
             'Perdedores' : [],
             'pontos_vencedor' : [],
             'pontos_perdedor' : [],
             'Data' : [],
             'Jogo' : [] }

cont = 1

for jogo in jogos: 

    vencedores_x = jogo.find('tr', class_ = 'winner')
    placar_vencedor = vencedores_x.find('td', class_ = 'right').text

    
    jogos_nba['pontos_vencedor'].append(placar_vencedor)

    vencedores = vencedores_x.find('a', href=True).text
    
    
    jogos_nba['Vencedores'].append(vencedores)


    perdedores_x = jogo.find('tr', class_ = 'loser')
    placar_perdedor = perdedores_x.find('td', class_ = 'right').text

    
    jogos_nba['pontos_perdedor'].append(placar_perdedor)

    perdedores = perdedores_x.find('a', href=True).text

    jogos_nba['Perdedores'].append(perdedores)

    jogos_nba['Data'].append(dia)
    jogos_nba['Data_Copy'] = jogos_nba['Data']
    jogos_nba['Jogo'].append(cont)
    cont += 1

jogos_nba_df = pd.DataFrame(jogos_nba)
jogos_nba_df = jogos_nba_df.set_index('Data')

file_path = 'partidas_NBA2024.xlsx'
df = pd.read_excel(file_path)
df = df.set_index('Data')
df = pd.concat([df, jogos_nba_df])
df2 = df.drop_duplicates(subset=['Data_Copy','Perdedores'])
df2.to_excel('partidas_NBA2024.xlsx')

