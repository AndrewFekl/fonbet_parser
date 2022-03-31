from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from parsers import GamesParser, get_md5_key

target_url = "https://www.fonbet.ru/live/"
games_url = 'https://line14.bkfon-resources.com/live/currentLine/ru'

games_parser = GamesParser(games_url)
sport_id_list = games_parser.get_sport_id_list()
games_dict = games_parser.get_live_footbol_matches(sport_id_list)

#for key, value in games_dict.items():
    #print(key, value, type(value))

last_match = games_dict.popitem()
link_text = last_match[1]
#byte_text1 = link_text.encode()

master_text = "Депортиво Масая — Пирукс Масатепе"
#byte_text2 = master_text.encode()

print(link_text)
print(master_text)
print(link_text == master_text)

"""print(byte_text1)
print(byte_text2)
print(byte_text1 == byte_text2)"""



def get_match_name(link_text):
    try:
        browser = webdriver.Chrome()
        browser.get(target_url)

        #link = browser.find_element(By.LINK_TEXT, "Депортиво Масая — Пирукс Масатепе")
        link = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        link.click()

        competition = browser.find_elements(By.CLASS_NAME, "ev-header__caption--1nhET")[2]
        print(competition.text)

    finally:
        # успеваем посмотреть переход на страницу за 10 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

get_match_name(link_text)






