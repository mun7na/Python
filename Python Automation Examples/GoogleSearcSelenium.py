from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Search_string = input("Input the URL or string you want to search : ")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
web.maximize_window()
for i in range(1):
    elements = web.get("https://www.google.com/search?q=" + Search_string + "&start=" + str(i))



