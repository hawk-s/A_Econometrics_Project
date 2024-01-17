import json

def load_sites_to_visit(file_name):
    """
    Load the list of functional page URLs from a JSON file.

    Args:
        file_name (str): The name of the JSON file.

    Returns:
        list: A list of functional page URLs.

    """
    with open(file_name, 'r') as file:
        sites_to_visit = json.load(file)

    return sites_to_visit

'''
# Usage example
functional_pages = load_sites_to_visit('sites_to_visit.json')
print(functional_pages)
'''