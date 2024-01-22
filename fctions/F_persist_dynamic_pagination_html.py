from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def persist_html_content_dynamic_pagination(urls, table_id, file_name='combined_data.html', wait_time=10):
    """
    Fetches the HTML content of web pages using Selenium, clicks through table pagination to ensure all data is loaded,
    and persists it as a single HTML document.

    Args:
        urls (list): List of URLs for the sites.
        table_id (str): The ID of the table to paginate through.
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

        # Wait for the initial table to load
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, table_id)))

        while True:
            # Get the HTML source of the current state of the page
            source = driver.page_source

            # Use BeautifulSoup to parse and clean the HTML
            soup = BeautifulSoup(source, 'lxml')

            # Append the HTML content to the combined HTML string
            combined_html += str(soup)

            # Check for and click the 'Next' button, break if not present
            try:
                next_button = driver.find_element_by_xpath("//a[@id='prices_next']")
                if "disabled" in next_button.get_attribute("class"):
                    break
                next_button.click()
                # Wait for the next set of data to load
                time.sleep(wait_time)
            except:
                break

    # Close the browser
    driver.quit()

    # Persist the combined HTML content as a single HTML file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(combined_html)

    print(f"HTML content persisted to {file_name}.")

# Usage example:
# sites_to_visit = ['http://example.com/tablepage1', 'http://example.com/tablepage2']
# table_id = "prices"  # Replace with the ID of your table
# persist_html_content_dynamic_pagination(sites_to_visit, table_id)
