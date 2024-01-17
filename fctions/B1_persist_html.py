import requests
from bs4 import BeautifulSoup


def persist_html_content(urls, file_name='combined_data.html'):
    """
    Fetches the HTML content of web pages and persists it as a single HTML document.

    Args:
        urls (list): List of corresponding URLs for the sites.
        file_name (str): The name of the output HTML file. Default is 'combined_data.html'.

    Returns:
        None
    """
    # Create an empty string to store the combined HTML content
    combined_html = ""

    for url in urls:
        # Send GET request to the URL and store the response
        response = requests.get(url)

        # Create a BeautifulSoup object from the content of the response
        soup = BeautifulSoup(response.content, 'lxml')

        # Append the HTML content to the combined HTML string
        combined_html += str(soup)

    # Persist the combined HTML content as a single HTML file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(combined_html)

    print(f"HTML content persisted to {file_name}.")

'''
# Usage:
sites_to_visit = load_sites_to_visit('sites_to_visit.json')
'''