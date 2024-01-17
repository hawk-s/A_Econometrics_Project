from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def persist_html_content_dynamic(urls, attribute_name, file_name='combined_data.html', wait_time=10):
    """
    Fetches the HTML content of web pages using Selenium, waiting for an element with a specified attribute,
    indicating AJAX content has loaded, and persists it as a single HTML document.

    Args:
        urls (list): List of corresponding URLs for the sites.
        attribute_name (str): The name of the attribute to wait for.
        file_name (str): The name of the output HTML file. Default is 'combined_data.html'.
        wait_time (int): Maximum time in seconds to wait. Default is 10 seconds.

    Returns:
        None
    """
    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    combined_html = ""

    for url in urls:
        # Load the URL
        driver.get(url)

        # Wait for an element with the specified attribute
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, f"//*[@{attribute_name}]")))

        # Get the HTML source of the page
        source = driver.page_source

        # Use BeautifulSoup to parse and clean the HTML
        soup = BeautifulSoup(source, 'lxml')

        # Append the HTML content to the combined HTML string
        combined_html += str(soup)

    # Close the browser
    driver.quit()

    # Persist the combined HTML content as a single HTML file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(combined_html)

    print(f"HTML content persisted to {file_name}.")

'''
# Usage example:
sites_to_visit = load_sites_to_visit('sites_to_visit.json')
attribute_name = "data-variant"  # Replace with the attribute you need to wait for
persist_html_content_dynamic(sites_to_visit, attribute_name)
'''
