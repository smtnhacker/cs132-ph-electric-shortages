import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://company.meralco.com.ph/news-and-advisories/maintenance-schedule")
driver.execute_script("window.scrollBy(0, 500);")

def attempt_click(element):
    while True:
        try:
            element.click()
            break
        except Exception as e:
            driver.execute_script("window.scrollBy(0, 20);")

def open_page(n=30):
    if n == 0:
        return
    
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bef-datepicker.form-text.form-control.hasDatepicker"))
    )

    attempt_click(date_picker)
    for _ in range(2):
        month_picker = driver.find_element(By.CLASS_NAME, "ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-all")
        prev_btn = month_picker.find_element(By.CLASS_NAME, "ui-datepicker-prev.ui-corner-all")
        attempt_click(prev_btn)

    calendar = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
    available_days = calendar.find_elements(By.CSS_SELECTOR, "td[data-handler='selectDay']")
    random_day = random.choice(available_days)
    attempt_click(random_day)
    time.sleep(0.5)

    try:
        warning = driver.find_element(By.CLASS_NAME, "alert.alert-warning")
        print("Has no scheduled maintenance", flush=True)
    except Exception:
        print("Has scheduled maintenance", flush=True)

    open_page(n-1)

def scrape_n_days(n=1):
    pass

if __name__ == '__main__':
    # data = scrape_n_days()
    open_page()