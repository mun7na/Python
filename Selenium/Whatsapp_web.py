from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web1 = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

# web1 = webdriver.Chrome()
web1.maximize_window()
# web.get("https://web.whatsapp.com/")





web1.get("https://www.python.org")
print(web1.title)
search_bar = web1.find_element("name", "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
print(web1.current_url)

web1.close()