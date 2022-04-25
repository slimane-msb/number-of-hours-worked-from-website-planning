import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from src.ShiftList import ShiftList
from src.shift import Shift

config = {
    'EMAIL': '',
    'PASSWORD': ''
}

login_url = 'https://app.skello.io/users/sign_in?lang=fr'

shifts = ShiftList()


def enter(elem):
    elem.send_keys(Keys.ENTER)
    time.sleep(1)


def click(elem):
    elem.click()
    time.sleep(1)


def get_date(driver):
    date_elem = driver.find_element_by_id("planningDate")
    day = date_elem.get_attribute('data-day')
    month = date_elem.get_attribute("data-month")
    year = date_elem.get_attribute("data-year")
    d1 = datetime.datetime(int(year), int(month), int(day))
    return d1


def date_ok(date):
    beginning_date = datetime.datetime(2021, 9, 25)
    return date > beginning_date


def date_before_today(date):
    today = datetime.today()
    print(date)
    return date < today


def check_date(driver):
    d1 = get_date(driver)
    print(d1)
    return date_ok(d1)


def before_today(driver):
    d1 = get_date(driver)
    return date_before_today(d1)



def get_prev_week(driver):
    prev_week = driver.find_element_by_xpath("//div[@id='calendar']/a/button")
    click(prev_week)


def add_time_to_shift_from_driver(driver, week_day_number, shift_number):
    td = driver.find_element_by_xpath("//table[@id='planning_week']/tbody/tr/td[" + str(week_day_number) + "]")
    date = td.get_attribute('data-date')
    date = date.split("T00")[0]
    shift = Shift(date)
    start = driver.find_element_by_xpath(
        "//table[@id='planning_week']/tbody/tr/td[" + str(week_day_number) + "]/div/div[" + str(shift_number) + "]/div[3]/div[1]/span/div/span[1]")
    end = driver.find_element_by_xpath(
        "//table[@id='planning_week']/tbody/tr/td[" + str(week_day_number) + "]/div/div[" + str(shift_number) + "]/div[3]/div[1]/span/div/span[3]")
    shift.add_start(start.text)
    shift.add_end(end.text)
    shift.add_title(get_shift_title(driver,week_day_number,shift_number))

    return shift


def get_shift_title(driver, week_day_number, shift_number):
    title_shift = driver.find_element_by_xpath(
        "//table[@id='planning_week']/tbody/tr/td[" + str(week_day_number) + "]/div/div[" + str(
            shift_number) + "]/div[3]/div[1]/span[2]")
    return title_shift.text


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get(login_url)

    # put username
    username = driver.find_element_by_xpath("//div[@class='col-12']/div/input")
    username.send_keys(config['EMAIL'])

    # put password
    password = driver.find_element_by_xpath("//div[@class='col-12']/div[2]/input")
    password.send_keys(config['PASSWORD'])

    # login enter
    connect = driver.find_element_by_xpath("//div[@class='col-12']/button")
    click(connect)

    # get week table
    first_week = 1
    while check_date(driver):
        for i in range(8, 1,-1):
            try:
                shift = add_time_to_shift_from_driver(driver, i, 1)
                if not shift.title == "Absence Autorisée":
                    shifts.add_shift(shift)
                print(shift)
                for j in range(2, 5):
                    try:
                        shift_sup = add_time_to_shift_from_driver(driver, i, j)
                        if not shift_sup.title == "Absence Autorisée":
                            shifts.add_shift(shift_sup)
                    except Exception as e:
                        pass
            except Exception as e:
                pass
        first_week = 0
        get_prev_week(driver)


    print(shifts)
    shifts.save_in_csv()

    time.sleep(10000)


if __name__ == '__main__':
    main()
