import schedule
import time
from Data_Scraper import auto_scrapper

def scheduler():
    schedule.every(1).hour.do(auto_scrapper)

    while True:
      schedule.run_pending()
      time.sleep(1)