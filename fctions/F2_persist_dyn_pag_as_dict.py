'''
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
'''
# Usage example
json_file_path = 'path_to_your_json_file.json'
with open(json_file_path, 'r') as file:
    urls_dict = json.load(file)

sets_html_content = fetch_html_content_with_pagination(urls_dict)
'''

'''
#updated fction to save the files and wait for the next button:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def fetch_html_content_with_pagination(urls_dict, output_directory, wait_time=10):
    """
    Fetches and combines HTML content of web pages with pagination using Selenium and saves them to files.

    Args:
        urls_dict (dict): A dictionary with set names as keys and list of URLs as values.
        output_directory (str): Directory where HTML files will be saved.
        wait_time (int): Maximum time in seconds to wait for page load. Default is 10 seconds.

    Returns:
        None
    """
    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for set_name, urls in urls_dict.items():
        combined_html = ""
        for url in urls:
            driver.get(url)
            WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')

            while True:
                source = driver.page_source
                soup = BeautifulSoup(source, 'lxml')
                combined_html += str(soup)

                try:
                    next_button = WebDriverWait(driver, wait_time).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'paginate_button next') and not(contains(@class, 'disabled'))]"))
                    )
                    next_button.click()
                    WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                except (TimeoutException, NoSuchElementException):
                    break

        # Save the combined HTML content to a file
        file_path = os.path.join(output_directory, f"{set_name}.html")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(combined_html)

    driver.quit()
    print(f"HTML content saved in directory: {output_directory}")
'''  
'''
# Usage example
json_file_path = 'path_to_your_json_file.json'
output_dir = 'path_to_your_output_directory'

with open(json_file_path, 'r') as file:
    urls_dict = json.load(file)

fetch_html_content_with_pagination(urls_dict, output_dir)
'''

#third and last update - for saving the files to the default directory (current)
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def fetch_html_content_with_pagination(urls_dict, output_directory=None, wait_time=10):
    """
    Fetches and combines HTML content of web pages with pagination using Selenium and saves them to files.

    Args:
        urls_dict (dict): A dictionary with set names as keys and list of URLs as values.
        output_directory (str, optional): Directory where HTML files will be saved. Defaults to current working directory.
        wait_time (int): Maximum time in seconds to wait for page load. Default is 10 seconds.

    Returns:
        None
    """
    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Use the current working directory if no output directory is specified
    if not output_directory:
        output_directory = os.getcwd()

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for set_name, urls in urls_dict.items():
        combined_html = ""
        for url in urls:
            driver.get(url)
            WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')

            while True:
                source = driver.page_source
                soup = BeautifulSoup(source, 'lxml')
                combined_html += str(soup)

                try:
                    next_button = WebDriverWait(driver, wait_time).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'paginate_button next') and not(contains(@class, 'disabled'))]"))
                    )
                    next_button.click()
                    WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                except (TimeoutException, NoSuchElementException):
                    break

        # Save the combined HTML content to a file
        file_path = os.path.join(output_directory, f"{set_name}.html")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(combined_html)

    driver.quit()
    print(f"HTML content saved in directory: {output_directory}")
'''
'''
# Usage example
json_file_path = 'path_to_your_json_file.json'
with open(json_file_path, 'r') as file:
    urls_dict = json.load(file)

fetch_html_content_with_pagination(urls_dict)
'''

##hmm, so the last time:): this time it saves each of the cards html separately 
#(since before it lead to an out of memory error...)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def fetch_html_content_with_pagination(urls_dict, output_directory=None, wait_time=10):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    if not output_directory:
        output_directory = os.getcwd()

    for set_name, urls in urls_dict.items():
        set_folder = os.path.join(output_directory, set_name)
        os.makedirs(set_folder, exist_ok=True)

        for index, url in enumerate(urls):
            driver.get(url)
            WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
            card_html = ""

            while True:
                source = driver.page_source
                soup = BeautifulSoup(source, 'lxml')
                card_html += str(soup)

                try:
                    next_button = WebDriverWait(driver, wait_time).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'paginate_button next') and not(contains(@class, 'disabled'))]"))
                    )
                    next_button.click()
                    WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                except (TimeoutException, NoSuchElementException):
                    break

            file_path = os.path.join(set_folder, f"card_{index + 1}.html")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(card_html)

    driver.quit()
    print(f"HTML content saved in directory: {output_directory}")
