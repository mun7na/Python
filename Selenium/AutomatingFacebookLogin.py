from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
web.maximize_window()

web.get('https://www.facebook.com/=true')

time.sleep(3)

Email = 'ma@gmail.com'
nam=web.find_element('xpath','//*[@id="login_form"]/div[2]/div[1]/label/input')
nam.send_keys(Email)
time.sleep(3)
Password = 'abcd'
nam1=web.find_element('xpath','//*[@id="login_form"]/div[2]/div[2]/label/input')
nam1.send_keys(Password)
time.sleep(3)
login =web.find_element('xpath','//*[@id="login_form"]/div[2]/div[3]/div/div/div[1]/div/span/span')
login.click()