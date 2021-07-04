# this program will take in a specific date from the user
# and will collect data from the highest scorer, highest assists,
# highest rebounder, and more stats from that specific date
# information taken from espn

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

print('PLEASE PRINT IN NUMBER FORMAT - mm/dd/yyyy')
month = int(input('enter the month: \n'))
day = int(input('enter the day: \n'))
year = int(input('enter the year: \n'))

# method to convert month into digit
def convert_month(month):
    if month < 10:
        month = str(month)
        month = '0' + month
    return month

# method to convert the days less than 10
def convert_day(day):
    if day < 10:
        day = str(day)
        day = '0' + day
    return day

# makes new url
def make_main_url():
    return main_url + str(year) + str(convert_month(month)) + str(convert_day(day))

# makes url for each game box score
def make_game_url(game_id):
    return game_url + str(game_id)

# TESTING DATE IS JANUARY 10, 2003 OR 01 10 2003

count = 0
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
main_url = 'https://www.espn.com/nba/scoreboard/_/date/'
game_url = 'https://www.espn.com/nba/boxscore/_/gameId/'
driver.get(make_main_url())

# looks for event, and only works after checking if it exists on the page after 10 seconds
try:
    game_list = []
    events = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "events"))
    )
    games = events.find_elements_by_class_name("scoreboard")
    for game in games:
        game_id = game.get_attribute('id')
        game_list.append(game_id) 
        count += 1
    for game in game_list:
        driver.execute_script("window.open(' ');")
        driver.get(make_game_url(game))

    print('total number of games = ' + str(count))
finally:
    # driver.quit()
    print('done')
