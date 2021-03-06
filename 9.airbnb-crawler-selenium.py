from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
from datetime import datetime


HOST = 'https://www.airbnb.co.kr/rooms/'


def run() :
    driver = webdriver.Chrome(executable_path="bin/chromedriver")
    f = open('airbnb_listings/airbnb_listings '+' '+str(datetime.now())+'.csv','w', newline='')
    csvWriter = csv.writer(f)

    for i in range(1135581, 1135581):
        driver.get(HOST+str(i))
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "listing_name"))
            )
            csvWriter.writerow(elem)
        finally:
            driver.quit()

        assert "Python" in driver.title
        elem = driver.find_element_by_id("listing_name")
#        elem.clear()
#        elem.send_keys("pycon")
#        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

run()
