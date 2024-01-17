from bs4 import BeautifulSoup

def load_html_document(file_name='combined_data.html', parser='html.parser'):
    """
    Loads and returns the content of an HTML document as a BeautifulSoup object.

    Args:
        file_name (str): The name of the HTML file to load. Default is 'combined_data.html'.
        parser (str): The parser to use for parsing the HTML. Default is 'lxml'.

    Returns:
        bs4.BeautifulSoup: The BeautifulSoup object representing the HTML document.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, parser)

    return soup
'''
# Example usage
loaded_html = load_html_document(file_name='combined_data.html', parser='html.parser')
print(loaded_html)
'''
