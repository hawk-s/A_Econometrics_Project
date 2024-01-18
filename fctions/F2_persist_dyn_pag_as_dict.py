from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

def fetch_html_content_with_pagination(urls_dict, wait_time=10):
    """
    Fetches and combines HTML content of web pages with pagination using Selenium.

    Args:
        urls_dict (dict): A dictionary with set names as keys and list of URLs as values.
        wait_time (int): Maximum time in seconds to wait for page load. Default is 10 seconds.

    Returns:
        dict: A dictionary with set names as keys and combined HTML content as values.
    """
    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    sets_html_dict = {}

    for set_name, urls in urls_dict.items():
        combined_html = ""
        for url in urls:
            driver.get(url)
            WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')

            while True:
                source = driver.page_source
                soup = BeautifulSoup(source, 'lxml')
                combined_html += str(soup)

                # Find and click the 'Next' button if it exists and is not disabled
                next_buttons = driver.find_elements(By.XPATH, "//a[contains(@class, 'paginate_button next') and not(contains(@class, 'disabled'))]")
                if next_buttons:
                    next_buttons[0].click()
                    WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                else:
                    break

        sets_html_dict[set_name] = combined_html

    driver.quit()
    return sets_html_dict

'''
# Usage example
json_file_path = 'path_to_your_json_file.json'
with open(json_file_path, 'r') as file:
    urls_dict = json.load(file)

sets_html_content = fetch_html_content_with_pagination(urls_dict)
'''