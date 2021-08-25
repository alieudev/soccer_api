import requests
from bs4 import BeautifulSoup
import json

# players = requests.get(
#     'https://www.worldfootball.net/teams/leicester-city/2022/2/').text
# soup = BeautifulSoup(players, 'html.parser')
# team_info = soup.find('table', class_='standard_tabelle').findAll(
#     'tr')

# leicester_city = []
# team_dict = {}
# leicester_city_pictures = {}

# for idx, player in enumerate(team_info):
#     try:
#         team_dict["Number"] = player.findAll('td')[1].text
#         team_dict["Name"] = player.findAll('td')[2].text
#         team_dict["Country"] = player.findAll('td')[4].text
#         team_dict["DOB"] = player.findAll('td')[5].text
#         team_dict["player_url_name"] = player.findAll(
#             'td')[0].a['href'].split('/')[2]
#         leicester_city.append(team_dict)
#         team_dict = {}
#     except:
#         pass

# print(leicester_city)
# team_players_with_pics_arr = []
# team_players_with_pics = {}

# for player in leicester_city:

#     name = player["player_url_name"]
#     person = requests.get(
#         "https://www.worldfootball.net/player_summary/{name}/".format(name=name)).text
#     soup = BeautifulSoup(person, 'html.parser')
#     img = soup.find('div', class_='sidebar').find(
#         'div', class_='data').img['src']
#     team_players_with_pics["Name"] = player["Name"]
#     team_players_with_pics["Number"] = player["Number"]
#     team_players_with_pics["Country"] = player["Country"]
#     team_players_with_pics["DOB"] = player["DOB"]
#     team_players_with_pics["Image"] = img
#     team_players_with_pics_arr.append(team_players_with_pics)
#     print('added info')
#     team_players_with_pics = {}
#     print('resting dict')

# print(team_players_with_pics_arr)


with open('leicester_city.json', 'w') as fp:
    data = [{'DOB': u'02/10/1984', 'Country': u'Switzerland', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/11070.jpg?fallback=png', 'Name': u'Eldin Jakupovi\u0107', 'Number': u'35'}, {'DOB': u'05/11/1986', 'Country': u'Denmark', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/24578.jpg?fallback=png', 'Name': u'Kasper Schmeichel', 'Number': u'1'}, {'DOB': u'22/06/1993', 'Country': u'Wales', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/199617.jpg?fallback=png', 'Name': u'Danny Ward', 'Number': u'12'}, {'DOB': u'13/07/1997', 'Country': u'Croatia', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/286420.jpg?fallback=png', 'Name': u'Filip Benkovi\u0107', 'Number': u'16'}, {'DOB': u'05/08/1989', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/67262.jpg?fallback=png', 'Name': u'Ryan Bertrand', 'Number': u'5'}, {'DOB': u'05/12/1995', 'Country': u'Belgium', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/239699.jpg?fallback=png', 'Name': u'Timothy Castagne', 'Number': u'27'}, {'DOB': u'03/01/1988', 'Country': u'Northern Ireland', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/58815.jpg?fallback=png', 'Name': u'Jonny Evans', 'Number': u'6'}, {'DOB': u'17/12/2000', 'Country': u'France', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/412529.jpg?fallback=png', 'Name': u'Wesley Fofana', 'Number': u'3'}, {'DOB': u'23/02/1998', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/340693.jpg?fallback=png', 'Name': u'James Justin', 'Number': u'2'}, {'DOB': u'06/10/1993', 'Country': u'Portugal', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/206500.jpg?fallback=png', 'Name': u'Ricardo Pereira', 'Number': u'21'}, {'DOB': u'23/05/1996', 'Country': u'Turkey', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/279175.jpg?fallback=png', 'Name': u'\xc7a\u011flar S\xf6y\xfcnc\xfc', 'Number': u'4'}, {'DOB': u'10/06/2001', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/411343.jpg?fallback=png', 'Name': u'Luke Thomas', 'Number': u'33'}, {'DOB': u'03/08/1992', 'Country': u'Denmark', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/169507.jpg?fallback=png', 'Name': u'Jannik Vestergaard', 'Number': u'23'}, {'DOB': u'18/11/1989', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/136085.jpg?fallback=png', 'Name': u'Marc Albrighton', 'Number': u'11'}, {'DOB': u'21/12/1994', 'Country': u'Ghana', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/233934.jpg?fallback=png', 'Name': u'Daniel Amartey', 'Number': u'18'}, {'DOB': u'09/12/1997', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/334081.jpg?fallback=png', 'Name': u'Harvey Barnes', 'Number': u'7'}, {'DOB': u'01/10/1997', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/328088.jpg?fallback=png', 'Name': u'Hamza Choudhury',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Number': u'20'}, {'DOB': u'06/09/1998', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/373722.jpg?fallback=png', 'Name': u'Kiernan Dewsbury-Hall', 'Number': u'22'}, {'DOB': u'23/11/1996', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/279837.jpg?fallback=png', 'Name': u'James Maddison', 'Number': u'10'}, {'DOB': u'23/06/1992', 'Country': u'France', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/170424.jpg?fallback=png', 'Name': u'Nampalys Mendy', 'Number': u'24'}, {'DOB': u'16/12/1996', 'Country': u'Nigeria', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/297625.jpg?fallback=png', 'Name': u'Wilfred Ndidi', 'Number': u'25'}, {'DOB': u'14/05/1994', 'Country': u'Belgium', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/192450.jpg?fallback=png', 'Name': u'Dennis Praet', 'Number': u'26'}, {'DOB': u'27/02/1999', 'Country': u'France', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/333865.jpg?fallback=png', 'Name': u'Boubakary Soumar\xe9', 'Number': u'42'}, {'DOB': u'08/01/2000', 'Country': u'Thailand', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/355222.jpg?fallback=png', 'Name': u'Thanawat Suengchitthawon', 'Number': u'64'}, {'DOB': u'07/05/1997', 'Country': u'Belgium', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/245962.jpg?fallback=png', 'Name': u'Youri Tielemans', 'Number': u'8'}, {'DOB': u'29/07/1993', 'Country': u'Spain', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/241838.jpg?fallback=png', 'Name': u'Ayoze P\xe9rez', 'Number': u'17'}, {'DOB': u'09/10/1998', 'Country': u'Zambia', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/310700.jpg?fallback=png', 'Name': u'Patson Daka', 'Number': u'29'}, {'DOB': u'03/10/1996', 'Country': u'Nigeria', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/256168.jpg?fallback=png', 'Name': u'Kelechi Iheanacho', 'Number': u'14'}, {'DOB': u'11/01/1987', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/201640.jpg?fallback=png', 'Name': u'Jamie Vardy', 'Number': u'9'}, {'DOB': u'26/01/1973', 'Country': u'Northern Ireland', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/132068.jpg?fallback=png', 'Name': u'Brendan Rodgers', 'Number': u''}, {'DOB': u'27/03/1985', 'Country': u'Wales', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/98002.jpg?fallback=png', 'Name': u'Chris Davies', 'Number': u''}, {'DOB': u'09/01/1980', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/486389.jpg?fallback=png', 'Name': u'Adam Sadler', 'Number': u''}, {'DOB': u'19/03/1981', 'Country': u'Ivory Coast', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/3516.jpg?fallback=png', 'Name': u'Kolo Tour\xe9', 'Number': u''}, {'DOB': u'19/04/1965', 'Country': u'England', 'Image': u'https://s.hs-data.com/bilder/spieler/gross/43379.jpg?fallback=png', 'Name': u'Mike Stowell', 'Number': u''}]
    json.dump(data, fp)
    print('data saved')
