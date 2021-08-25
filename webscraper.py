import requests
from bs4 import BeautifulSoup
import time

# res = requests.get(
#     'https://www.footballhistory.org/league/premier-league.html')
# print(res.status_code)
# soup = BeautifulSoup(res.text, 'html.parser')
# team_info = soup.find_all('table')[4]
# club_info = {}
# print(type(team_info))

# response = requests.get(
#     'https://www.worldfootball.net/teams/leicester-city/2022/2/').text
# soup = BeautifulSoup(response, 'html.parser')
# players = soup.find('div', 'portfolio')
# player_data = {}
# players_info = players.a.findAll('img')
# print(players_info)
# for player in players:


# titles = []
# for info in infos.tr:
#     titles.append(info.text)

# print(titles)


# players = []
# for player in infos:
#     players.append(player.a.text)
# print(players)

# player
player = requests.get(
    'https://www.worldfootball.net/player_summary/eldin-jakupovic/').text
soup = BeautifulSoup(player, 'html.parser')
img = soup.find('div', class_='sidebar')
print(img.find('div', class_='data').img['src'])
