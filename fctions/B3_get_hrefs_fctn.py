from bs4 import BeautifulSoup
from B2_load_html_fctn import load_html_document

def extract_href_with_prefix(soup, tag='a', prefix='/celebnetworth/', class_name=''):
    """
    Extracts the href values from specified tags in the BeautifulSoup object that start with the specified prefix and have the specified class (if provided).

    Args:
        soup (bs4.BeautifulSoup): The BeautifulSoup object representing the HTML content.
        tag (str): The name of the tag to search for href values. Default is 'a'.
        prefix (str): The prefix that the href values should start with. Default is '/celebnetworth/'.
        class_name (str): The class name that the tag should have. Default is an empty string.

    Returns:
        list: A list of href values that match the specified criteria.
    """
    tags = soup.find_all(tag, class_=class_name, href=lambda href: href.startswith(prefix) and len(href) > len(prefix))
    hrefs = [t['href'] for t in tags]
    return hrefs
'''
# Example usage
loaded_html = load_html_document(file_name='combined_data.html')
hrefs = extract_href_with_prefix(loaded_html, tag='a', prefix='/celebnetworth/', class_name='')
print(hrefs)
'''