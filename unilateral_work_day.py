import urllib3
import selenium
import requests
from selenium.webdriver.common.keys import Keys
import webbrowser
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from _datetime import datetime
#ELEMENTAL XPATHS
driver = webdriver.Chrome()



driver.get('https://www5.elawsoftware.com/eLawSecure.nsf/SecureLogin?ReadForm')#put here the address of your page

user1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/input"
pass1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[2]/td[3]/input"
access_server_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/div/input"


#find the elements to click and interact with
user1 = driver.find_element_by_xpath(user1_XPATH)
pass1 = driver.find_element_by_xpath(pass1_XPATH)
access1 = driver.find_element_by_xpath(access_server_XPATH)
user1.send_keys("")
pass1.send_keys("")
access1.click()
urlform2 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&t=1"
urlform3 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&Seq=1&t=1"
driver.get(urlform2)

#date logic
dt = datetime.now()
tmrw_day_int = int(dt.day) + 1
tmrw_day = str(tmrw_day_int)
tmrw_month = str(dt.month)
tmrw_yr = str(dt.year)
ds = "/"
entered_date = tmrw_month + ds + tmrw_day + ds +tmrw_yr
docket_date1 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[1]/input")
docket_date2 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[2]/input")

def replace_values2():
    docket_date1.clear()
    docket_date1.send_keys(entered_date)
    docket_date2.clear()
    docket_date2.send_keys(entered_date)

replace_values2()
urlform3_XPATH = "//*[@id=\"menu0\"]"

driver.find_element_by_xpath(urlform3_XPATH).click()

def print2():
    keyboard.press_and_release('cmd+p')
    keyboard.press_and_release('enter')
print2()
driver.close()
