import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

warriors, bucks, lakers, celtics, ers, hawks, magic, nets, pacers, bulls, cavaliers, knicks, raptors, pistons, wizards, hornets, heat, mavericks, nuggets, pelicans, thunder, spurs, clippers, timberwolves, kings, suns, blazers, jazz, rockets, grizzlies = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}

class NBA:
    def __init__(self, url, dicionario, nome):
        self.url = url
        self.dicionario = dicionario
        self.nome = nome
        self.names = ['wins', 'losses', 'rank_team', 'avg_age', 'avg_ht', 'avg_wt', 'g', 'mp_per_g', 'fg_per_g', 'fga_per_g', 'fg_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'fg2_per_g', 'fg2a_per_g', 'fg2_pct', 'ft_per_g', 'fta_per_g', 'ft_pct', 'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g']

    def modelo(self):
        a_res = requests.get(self.url)
        bucks_soup = BeautifulSoup(a_res.content, 'lxml')
        main = bucks_soup.find(name="tbody")
        cont = 0
        cont2 = 0

        for row in main.find_all('tr'):
            cont += 1
            if cont == 1:
                for name in self.names:
                    if cont2 == 0:
                        cont2 += 1
                        self.dicionario = {}
                    self.dicionario[name] = row.find(name='td', attrs={'data-stat': name}).text

        self.data = pd.DataFrame(self.dicionario, index=[self.nome])

    def get_data(self):
        return self.data
    

celtics_time = NBA("https://www.basketball-reference.com/teams/BOS/stats_per_game_totals.html" , celtics, "Boston Celtics")
celtics_time.modelo()
celtics_df = celtics_time.get_data()

ers_time = NBA("https://www.basketball-reference.com/teams/PHI/stats_per_game_totals.html" , ers, "Philadelphia 76ers")
ers_time.modelo()
ers_df = ers_time.get_data()

nets_time = NBA("https://www.basketball-reference.com/teams/NJN/stats_per_game_totals.html" , nets, "Brooklyn Nets")
nets_time.modelo()
nets_df = nets_time.get_data()

magic_time = NBA("https://www.basketball-reference.com/teams/ORL/stats_per_game_totals.html" , magic, "Orlando Magic")
magic_time.modelo()
magic_df = magic_time.get_data()

bucks_time = NBA("https://www.basketball-reference.com/teams/MIL/stats_per_game_totals.html" , bucks, "Milwaukee Bucks,")
bucks_time.modelo()
bucks_df = bucks_time.get_data()

hawks_time = NBA("https://www.basketball-reference.com/teams/ATL/stats_per_game_totals.html" , hawks, "Atlanta Hawks")
hawks_time.modelo()
hawks_df = hawks_time.get_data()

pacers_time = NBA("https://www.basketball-reference.com/teams/IND/stats_per_game_totals.html" , pacers, "Indiana Pacers")
pacers_time.modelo()
pacers_df = pacers_time.get_data()

heat_time = NBA("https://www.basketball-reference.com/teams/MIA/stats_per_game_totals.html" , heat, "Miami Heat")
heat_time.modelo()
heat_df = heat_time.get_data()

raptors_time = NBA("https://www.basketball-reference.com/teams/TOR/stats_per_game_totals.html" , raptors, "Toronto Raptors")
raptors_time.modelo()
raptors_df = raptors_time.get_data()

knicks_time = NBA("https://www.basketball-reference.com/teams/NYK/stats_per_game_totals.html" , knicks, "New York Knicks")
knicks_time.modelo()
knicks_df = knicks_time.get_data()

bulls_time = NBA("https://www.basketball-reference.com/teams/CHI/stats_per_game_totals.html" , bulls, "Chicago Bulls")
bulls_time.modelo()
bulls_df = bulls_time.get_data()

cavaliers_time = NBA("https://www.basketball-reference.com/teams/CLE/stats_per_game_totals.html" , cavaliers, "Cleveland Cavaliers")
cavaliers_time.modelo()
cavaliers_df = cavaliers_time.get_data()

pistons_time = NBA("https://www.basketball-reference.com/teams/DET/stats_per_game_totals.html" , pistons, "Detroit Pistons")
pistons_time.modelo()
pistons_df = pistons_time.get_data()

hornets_time = NBA("https://www.basketball-reference.com/teams/CHA/stats_per_game_totals.html" , hornets, "Charlotte Hornets")
hornets_time.modelo()
hornets_df = hornets_time.get_data()

wizards_time = NBA("https://www.basketball-reference.com/teams/WAS/stats_per_game_totals.html" , wizards, "Washington Wizards")
wizards_time.modelo()
wizards_df = wizards_time.get_data()

warriors_time = NBA("https://www.basketball-reference.com/teams/GSW/stats_per_game_totals.html" , warriors, "Golden State Warriors")
warriors_time.modelo()
warriors_df = warriors_time.get_data()

nuggets_time = NBA("https://www.basketball-reference.com/teams/DEN/stats_per_game_totals.html" , nuggets, "Denver Nuggets")
nuggets_time.modelo()
nuggets_df = nuggets_time.get_data()

pelicans_time = NBA("https://www.basketball-reference.com/teams/NOH/stats_per_game_totals.html" , pelicans, "New Orleans Pelicans")
pelicans_time.modelo()
pelicans_df = pelicans_time.get_data()

mavericks_time = NBA("https://www.basketball-reference.com/teams/DAL/stats_per_game_totals.html" , mavericks, "Dallas Mavericks")
mavericks_time.modelo()
mavericks_df = mavericks_time.get_data()

lakers_time = NBA("https://www.basketball-reference.com/teams/LAL/stats_per_game_totals.html" , lakers, "Los Angeles Lakers")
lakers_time.modelo()
lakers_df = lakers_time.get_data()

spurs_time = NBA("https://www.basketball-reference.com/teams/SAS/stats_per_game_totals.html" , spurs, "San Antonio Spurs")
spurs_time.modelo()
spurs_df = spurs_time.get_data()

clippers_time = NBA("https://www.basketball-reference.com/teams/LAC/stats_per_game_totals.html" , clippers, "Los Angeles Clippers")
clippers_time.modelo()
clippers_df = clippers_time.get_data()

thunder_time = NBA("https://www.basketball-reference.com/teams/OKC/stats_per_game_totals.html" , thunder, "Oklahoma City Thunder")
thunder_time.modelo()
thunder_df = thunder_time.get_data()

blazers_time = NBA("https://www.basketball-reference.com/teams/POR/stats_per_game_totals.html" , blazers, "Portland Trail Blazers")
blazers_time.modelo()
blazers_df = blazers_time.get_data()

timberwolves_time = NBA("https://www.basketball-reference.com/teams/MIN/stats_per_game_totals.html" , timberwolves, "Minnesota Timberwolves")
timberwolves_time.modelo()
timberwolves_df = timberwolves_time.get_data()

kings_time = NBA("https://www.basketball-reference.com/teams/SAC/stats_per_game_totals.html" , kings, "Sacramento Kings")
kings_time.modelo()
kings_df = kings_time.get_data()

suns_time = NBA("https://www.basketball-reference.com/teams/PHO/stats_per_game_totals.html" , suns, "Phoenix Suns")
suns_time.modelo()
suns_df = suns_time.get_data()

jazz_time = NBA("https://www.basketball-reference.com/teams/UTA/stats_per_game_totals.html" , jazz, "Utah Jazz")
jazz_time.modelo()
jazz_df = jazz_time.get_data()

rockets_time = NBA("https://www.basketball-reference.com/teams/HOU/stats_per_game_totals.html" , rockets, "Houston Rockets")
rockets_time.modelo()
rockets_df = rockets_time.get_data()

grizzlies_time = NBA("https://www.basketball-reference.com/teams/MEM/stats_per_game_totals.html" , grizzlies, "Memphis Grizzlies")
grizzlies_time.modelo()
grizzlies_df = grizzlies_time.get_data()

dataframes = pd.concat([celtics_df , ers_df , hawks_df , magic_df , nets_df , pacers_df , bulls_df , cavaliers_df , knicks_df , raptors_df , pistons_df , wizards_df , hornets_df , heat_df , mavericks_df , warriors_df , nuggets_df , pelicans_df , thunder_df , lakers_df , spurs_df , clippers_df , timberwolves_df , kings_df , suns_df , blazers_df , jazz_df , rockets_df , grizzlies_df ])
dataframes.to_excel('NBA2024.xlsx')
