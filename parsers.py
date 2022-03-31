import hashlib
import requests


# Адрес для парсинга информации
games_url = 'https://line14.bkfon-resources.com/live/currentLine/ru'

def get_md5_key(id, gamer_name):
    """ Функция принимает id матча и строку вида Игрок1 - Игрок2 и возвращает md5 хэш"""

    key_str = str(id) + gamer_name
    hash_object = hashlib.md5(key_str.encode())
    return hash_object.hexdigest()


class GamesParser():
    """ Класс парсера данных о матчах на Фонбет в режиме Live.
    Объект класса инициализируется с передачей url api и содержит два метода - получения id соревнований
    и собственно списка футбольных матчей"""


    def __init__(self, games_url):

        self.games_url = games_url


    def get_sport_id_list(self):
        """ Получаем список id футбольных соревнований """

        sport_id_list = []
        sports_list = requests.get(self.games_url).json()["sports"]
        for line in sports_list:

            competition = line["name"]
            id = line["id"]
            #print(id, competition,'\n')

            if 'Футбол' in competition:
                sport_id_list.append(id)

        return sport_id_list


    def get_live_footbol_matches(self, sport_id_list):
        """ Получаем словарь футбольных матчей в Live. Ключи словаря хэш от id матча и
         строки названий команд игроков """

        live_footbol_games = {}
        matches = requests.get(self.games_url).json()["events"]

        for line in matches:

            if line["place"] == "live":
                if line["level"] == 1:
                    if line["sportId"] in sport_id_list:

                        id = line["id"]
                        team1 = str(line["team1"]).strip()
                        team2 = str(line["team2"]).strip()
                        tire_b = b' \xe2\x80\x94 '
                        tire = tire_b.decode()
                        gamer_name = team1 + tire +team2
                        key = get_md5_key(id, "some thing")
                        live_footbol_games.update({key: gamer_name})

        return live_footbol_games


if __name__ == "__main__":

    games_parser = GamesParser(games_url)

    sport_id_list = games_parser.get_sport_id_list()

    games_dict = games_parser.get_live_footbol_matches(sport_id_list)
    print(games_dict)







