import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


wiz_url = (f'https://www.basketball-reference.com/leagues/NBA_2024.html')

# The requests library can send a GET request to the wiz_url
wiz_res = requests.get(wiz_url)

# BeautifulSoup library parses the content of an HTML document, in this case wiz_res
wiz_soup = BeautifulSoup(wiz_res.content, 'lxml')

# BeautifulSoup's .find() method searches for a tag and specified attributes, 
# returning the first match 
wiz_per_game = wiz_soup.find_all('tbody')

for tbody in wiz_per_game:
    x = tbody.find_all('a', href=True)

    for link in x:
        print({link['href']})

    y = tbody.find_all(name = 'a')

    for name in y:
        print({name.text})




links_beta = ['/teams/BOS/2024.html',
'/teams/PHI/2024.html',
'/teams/BRK/2024.html',
'/teams/ORL/2024.html',
'/teams/MIL/2024.html',
'/teams/ATL/2024.html',
'/teams/IND/2024.html',
'/teams/MIA/2024.html',
'/teams/TOR/2024.html',
'/teams/NYK/2024.html',
'/teams/CHI/2024.html',
'/teams/CLE/2024.html',
'/teams/DET/2024.html',
'/teams/CHO/2024.html',
'/teams/WAS/2024.html',
'/teams/BOS/2024.html',
'/teams/PHI/2024.html',
'/teams/BRK/2024.html',
'/teams/TOR/2024.html',
'/teams/NYK/2024.html',
'/teams/MIL/2024.html',
'/teams/IND/2024.html',
'/teams/CHI/2024.html',
'/teams/CLE/2024.html',
'/teams/DET/2024.html',
'/teams/ORL/2024.html',
'/teams/ATL/2024.html',
'/teams/MIA/2024.html',
'/teams/CHO/2024.html',
'/teams/WAS/2024.html']


time_nomes = ['Boston Celtics',
'Philadelphia 76ers',
'Brooklyn Nets',
'Orlando Magic',
'Milwaukee Bucks,',
'Atlanta Hawks',
'Indiana Pacers',
'Miami Heat',
'Toronto Raptors',
'New York Knicks',
'Chicago Bulls',
'Cleveland Cavaliers',
'Detroit Pistons',
'Charlotte Hornets',
'Golden State Warriors',
'Denver Nuggets',
'New Orleans Pelicans',
'Dallas Mavericks',
'Los Angeles Lakers',
'San Antonio Spurs',
'Los Angeles Clippers',
'Oklahoma City Thunder',
'Portland Trail Blazers',
'Minnesota Timberwolves',
'Sacramento Kings',
'Phoenix Suns',
'Utah Jazz',
'Houston Rockets',
'Memphis Grizzlies',]