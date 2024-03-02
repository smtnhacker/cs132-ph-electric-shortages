import os
import time
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

class DataRow:
    def __init__(self, date, has_outage):
        self.date = date
        self.has_outage = 1 if has_outage else 0
    
    def __str__(self):
        return f"{self.date},{self.has_outage}\n"

def attempt_click(element):
    tries = 0
    while True:
        try:
            element.click()
            break
        except Exception as e:
            # print(e, flush=True)
            driver.execute_script("window.scrollBy(0, 20);")
            tries += 1
            if tries == 20:
                print(e, flush=True)

def has_maintanance():
    try:
        warning = driver.find_element(By.CLASS_NAME, "alert.alert-warning")
        return False
    except Exception:
        return True

def scrape_n_days(n=1):
    driver.get("https://company.meralco.com.ph/news-and-advisories/maintenance-schedule")
    driver.execute_script("window.scrollBy(0, 500);")

    cur_date = date.today()

    # get the data for today
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bef-datepicker.form-text.form-control.hasDatepicker"))
    )
    attempt_click(date_picker)
    calendar = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
    cur_day_btn = calendar.find_element(By.CLASS_NAME, "ui-datepicker-days-cell-over.ui-datepicker-today")
    attempt_click(cur_day_btn)

    yield DataRow(date=cur_date, has_outage=has_maintanance())

    # get the previous days
    for day in range(n-1):
        cur_date = cur_date - timedelta(days=1)
        time.sleep(1)

        # go to previous day
        date_picker = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bef-datepicker.form-text.form-control.hasDatepicker"))
        )
        attempt_click(date_picker)
        calendar = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
        available_days = calendar.find_elements(By.CSS_SELECTOR, "td[data-handler='selectDay']")
        prev_day = None
        for day in available_days:
            if "ui-datepicker-current-day" in day.get_attribute("class"):
                break
            prev_day = day
        
        if prev_day == None:
            time.sleep(1)
            date_picker = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bef-datepicker.form-text.form-control.hasDatepicker"))
            )
            attempt_click(date_picker)
            month_picker = driver.find_element(By.CLASS_NAME, "ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-all")
            prev_btn = month_picker.find_element(By.CLASS_NAME, "ui-datepicker-prev.ui-corner-all")
            attempt_click(prev_btn)
            time.sleep(1)

            date_picker = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "bef-datepicker.form-text.form-control.hasDatepicker"))
            )
            attempt_click(date_picker)
            calendar = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
            available_days = calendar.find_elements(By.CSS_SELECTOR, "td[data-handler='selectDay']")
            last_day = available_days[-1]
            attempt_click(last_day)
        else:
            attempt_click(prev_day)

        yield DataRow(date=cur_date, has_outage=has_maintanance())

def main():
    if not os.path.isdir(os.path.join("data-gathering", "data")):
        os.makedirs("data")
    
    filepath = os.path.join("data-gathering", "data", "output.txt")
    # empties the current output
    # so be CAREFUL!!!
    open(filepath, 'w').close()

    for dataRow in scrape_n_days(n=100):
        with open(filepath, 'a') as f:
            f.write(str(dataRow))
    
    print("Finished scraping!")

if __name__ == '__main__':
    main()