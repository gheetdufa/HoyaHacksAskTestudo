from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def scrape_page_with_selenium(url, depth=0):
    chrome_service = ChromeService(executable_path="/Users/utsav/Downloads/chromedriver-mac-arm64/chromedriver")

    with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
        driver.get(url)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        title = driver.title
        content = driver.find_element(By.TAG_NAME, 'body').text

        with open('planetterp.txt', 'a', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"URL: {url}\n")
            file.write("Content:\n")
            file.write(content + '\n' + '-' * 30 + '\n')

        if depth > 0:
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                link_url = link.get_attribute('href')
                if link_url:
                    internal_link = link_url
                    scrape_page_with_selenium(internal_link, depth - 1)

def job():
    url = 'https://umd.edu/'
    scrape_page_with_selenium(url, depth=2)

# Schedule the job to run every day at 12 pm
schedule.every().day.at("12:00").do(job)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)