# this program will take in a specific date from the user
# and will collect data from the highest scorer, highest assists,
# highest rebounder, and more stats from that specific date
# information taken from espn

import selenium
from selenium import webdriver

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
def make_url():
    return url + str(year) + str(convert_month(month)) + str(convert_day(day))

# TESTING DATE IS JANUARY 10, 2003 OR 01 10 2003
# print(make_url())
count = 0
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = 'https://www.espn.com/nba/scoreboard/_/date/'
driver.get(make_url())

# events = driver.find_elements_by_xpath('//*[@id="events"]')

# scoreboard = driver.find_elements_by_css_selector('scoreboard basketball final home-winner js-show')

button_numbers = driver.find_elements_by_xpath("//*[@div ='events']//a[contains(@href, 'boxscore')]")
print(len(button_numbers))

# link = driver.find_element_by_xpath('//*[@id="230110006"]/div/section/a[2]')
# link.click()
# points = driver.find_element_by_xpath('')
# print(points.text)