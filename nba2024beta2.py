nome_time = ['celtics', 'ers' , 'nets', 'magic', 'bucks', 'hawks', 'pacers', 'heat', 'raptors', 'knicks', 'bulls', 'cavaliers', 'pistons', 'hornets', 'wizards', 'warriors','nuggets', 'pelicans','mavericks','lakers', 'spurs', 'clippers','thunder','blazers', 'timberwolves', 'kings', 'suns', 'jazz', 'rockets', 'grizzlies']
links_beta = ['/teams/BOS/',
'/teams/PHI/',
'/teams/BRK/',
'/teams/ORL/',
'/teams/MIL/',
'/teams/ATL/',
'/teams/IND/',
'/teams/MIA/',
'/teams/TOR/',
'/teams/NYK/',
'/teams/CHI/',
'/teams/CLE/',
'/teams/DET/',
'/teams/CHA/',
'/teams/WAS/',
'/teams/GSW/',
'/teams/DEN/',
'/teams/NOP/',
'/teams/DAL/',
'/teams/LAL/',
'/teams/SAS/',
'/teams/LAC/',
'/teams/OKC/',
'/teams/POR/',
'/teams/MIN/',
'/teams/SAC/',
'/teams/PHO/',
'/teams/UTA/',
'/teams/HOU/',
'/teams/MEM/']


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
'Washington Wizards',
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

somatorio = []
contador1 = 0
contador2 = 1
definitivo = []

'https://www.basketball-reference.com/teams/MIL/stats_per_game_totals.html'
for n in nome_time:
    print(f'{n}_time = NBA("https://www.basketball-reference.com{links_beta[contador1]}stats_per_game_totals.html" , {n}, "{time_nomes[contador1]}")')
    print(f'{n}_time.modelo()')
    print(f'{n}_df = {n}_time.get_data()')
    print()
    contador1 += 1


'''for n in nome_time:
    somatorio.append(n + '_df')

for n in somatorio:
    if contador2 == 1:
        print(f'[{n} ,', end='')

    if contador2 == 29:
        print(f'{n} ]', end='')
    else:
        print(f'{n} , ', end='')

    contador2 += 1'''
