from selenium import webdriver

search_string = input("Input the URL or string you want to search : ")

driver= webdriver.Firefox()

for i in range(1):
    elements = driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
#https://www.google.com/search? q=1&start=0
#Chromedriver is not working