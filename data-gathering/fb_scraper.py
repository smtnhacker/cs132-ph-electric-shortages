from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

driver = webdriver.Chrome()
load_dotenv()

class Scraper:
    def __init__(self):
        driver = webdriver.Chrome()
        self.fbuser = os.getenv("FACEBOOK_USER")
        self.fbpass = os.getenv("FACEBOOK_PASS")

        if self.fbuser and self.fbpass:
            self.login()
        else:
            print("Running without authentication!")

    def login(self):
        driver.get("https://www.facebook.com")
        ulog = driver.find_element(By.ID, "email")
        plog = driver.find_element(By.ID, "pass")
        ulog.send_keys(self.fbuser)
        plog.send_keys(self.fbpass)
        button = driver.find_element(By.NAME, "login")
        button.click()
        # Handle succesfull login somehow.


    def scrape_routine(self, url):
        driver.get(url)


scraper = Scraper()