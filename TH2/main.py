from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

time_sleep = random.randint(2,8)
# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")

# 2. Mở thử một trang web
browser.get("http://youtube.com")

sigin_button = browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a")
sigin_button.click()
sleep(random.randint(5,10))

login_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
login_button.click()

email_txt = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email_txt.send_keys("hoangtuyenblogger@gmail.com")

next_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
next_button.click()

