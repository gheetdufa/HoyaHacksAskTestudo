from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def scrape_page_with_selenium(url, depth=0):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_service = ChromeService(executable_path="/Users/utsav/Downloads/chromedriver-mac-arm64/chromedriver")  # Specify the path to your chromedriver executable

    with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
        driver.get(url)
        
        # Wait for dynamic content to be loaded (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Extract information based on your needs
        title = driver.title
        content = driver.find_element(By.TAG_NAME, 'body').text

        # Save information to a text file
        with open('planetterp.txt', 'a', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"URL: {url}\n")
            file.write("Content:\n")
            file.write(content + '\n' + '-' * 30 + '\n')

        # Extract internal links and recursively scrape them
        if depth > 0:
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                link_url = link.get_attribute('href')
                if link_url:
                    internal_link = link_url
                    scrape_page_with_selenium(internal_link, depth - 1)

# URL of the college website
url = 'https://planetterp.com/'

# Call the function to start scraping
scrape_page_with_selenium(url, depth=2)