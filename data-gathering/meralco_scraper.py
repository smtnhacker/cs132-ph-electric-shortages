import os
import time
import traceback
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

class DataRow:
    def __init__(self, date, affected_locs):
        self.date = date
        self.affected_locs = affected_locs
    
    def __str__(self):
        return f'{self.date},"{self.affected_locs}"\n'

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
    """
    Returns if a specific date has an outage
    """
    try:
        warning = driver.find_element(By.CLASS_NAME, "alert.alert-warning")
        return False
    except Exception:
        return True

def get_affected_locs(cur_date):
    try:
        titles = set()
        page = 0
        while True:
            url = f'https://company.meralco.com.ph/news-and-advisories/maintenance-schedule?field_service_maintenance_loc_target_id=All&date_range_filter={cur_date}&page={page}'
            try:
                driver.get(url)
                time.sleep(1)
                posts = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "views-infinite-scroll-content-wrapper.clearfix"))
                )
                titles |= set(x.get_attribute("innerHTML") for x in posts.find_elements(By.CSS_SELECTOR, "a[class='text-default']"))
            except Exception:
                break
            page += 1
        affected_locs = list(titles)
        return affected_locs
    except Exception as e:
        return []

def scrape_n_days(n=1):
    driver.get("https://company.meralco.com.ph/news-and-advisories/maintenance-schedule")
    driver.execute_script("window.scrollBy(0, 500);")

    cur_date = date.today()

    # get the previous days
    for day in range(n):
        cur_date = cur_date - timedelta(days=1)
        time.sleep(1)
        formatted_date = cur_date.strftime("%m/%d/%Y")
        for affected_locs in get_affected_locs(formatted_date):
            yield DataRow(date=cur_date, affected_locs=affected_locs)

def main():
    if not os.path.isdir(os.path.join("data-gathering", "data")):
        os.makedirs(os.path.join("data-gathering", "data"))
    
    filepath = os.path.join("data-gathering", "data", "output.txt")
    # empties the current output
    # so be CAREFUL!!!
    open(filepath, 'w').close()

    start_time = time.time()

    for dataRow in scrape_n_days(n=10):
        with open(filepath, 'a') as f:
            f.write(str(dataRow))
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Finished scraping in {elapsed_time} seconds!")

if __name__ == '__main__':
    main()