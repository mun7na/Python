from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)




web = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
web.get('https://docs.google.com/forms/d/1kJ5t-vK-uH3pNenFudQtJk8MrtPalbKjhLjDc08Dcdk/viewform?edit_requested=true')


time.sleep(3)

# sign =web.find_element('xpath','/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
# sign.click()
# time.sleep(2)
# email1="munna7.pen@gmail.com"
# emailogin =web.find_element('xpath','//*[@id="identifierId"]')
# emailogin.send_keys(email1)
# time.sleep(2)
# next =web.find_element('xpath','//*[@id="identifierNext"]/div/button/span')
# next.click()
# email =web.find_element('xpath','//*[@id="i5"]')
# email.click()


Your_name = 'Sadman'
nam=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
nam.send_keys(Your_name)

time.sleep(3)

Attendance_Status =web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
Attendance_Status.click()

time.sleep(3)

Attendance_Type =web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
Attendance_Type.click()

time.sleep(3)

Your_department =web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span')
Your_department.click()

time.sleep(3)

Submit =web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
Submit.click()

