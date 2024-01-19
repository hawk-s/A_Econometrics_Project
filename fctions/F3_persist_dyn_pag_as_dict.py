#fction that is able from a certain name of the set in the dictionary and go on from that set
#also it should not wait for 10 seconds once it reaches the end of the table but go immediately to another url
#and finally it should create numbered folders (to avoid rewriting of existent folders)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def fetch_html_content_with_pagination_2(urls_dict, start_set_name, output_directory=None, wait_time=10):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    if not output_directory:
        output_directory = os.getcwd()

    start_processing = False  # Flag to indicate when to start processing
    folder_counter = 2  # Start numbering from 2

    for set_name, urls in urls_dict.items():
        if set_name == start_set_name:
            start_processing = True  # Start processing when the set name matches

        if not start_processing:
            continue  # Skip until the specified set name is found

        numbered_set_folder = f"{folder_counter}_{set_name}"  # Prefix the set name with a number
        set_folder = os.path.join(output_directory, numbered_set_folder)
        os.makedirs(set_folder, exist_ok=True)
        folder_counter += 1  # Increment the counter for the next set

        for index, url in enumerate(urls):
            driver.get(url)
            WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
            card_html = ""

            while True:
                source = driver.page_source
                soup = BeautifulSoup(source, 'lxml')
                card_html += str(soup)

                try:
                    next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'paginate_button next') and not(contains(@class, 'disabled'))]")
                    if next_button:
                        next_button.click()
                        WebDriverWait(driver, wait_time).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                    else:
                        break
                except (TimeoutException, NoSuchElementException):
                    break

            file_path = os.path.join(set_folder, f"card_{index + 1}.html")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(card_html)

    driver.quit()
    print(f"HTML content saved in directory: {output_directory}")


'''
# Example of how to call the function
urls_dict = {'Set1': ['url1', 'url2'], 'Set2': ['url3', 'url4']}
fetch_html_content_with_pagination_2(urls_dict, start_set_name='Set2')
'''