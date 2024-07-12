# import requests
# r=requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
# print(r)
# print(r.content)


import schedule
import time

def func():
    print("Geeksforgeeks")

schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)
