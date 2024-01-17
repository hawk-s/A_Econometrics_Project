import requests
import json
#from C1_json_writer import write_to_json

def filter_functional_urls(urls):
    """
    Filter a list of URLs to get only the functional ones.

    Args:
        urls (list): A list of URLs to check.

    Returns:
        list: A list of functional URLs.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the GET request.
    """
    functional_urls = []

    for url in urls:
        try:
            # Send a GET request and check the status code
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes

            functional_urls.append(url)
        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection error, timeout)
            print(f"An error occurred while accessing {url}: {e}")

    return functional_urls

'''
# Example usage
urls_to_check = [
    "https://example.com/page1",
    "https://example.com/page2",
    # Add more URLs here
]
functional_urls = filter_functional_urls(urls_to_check)
print(functional_urls)

# Save the list to a JSON file using the write_to_json function
write_to_json('functional_urls.json', functional_urls)
'''