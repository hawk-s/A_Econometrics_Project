import json

def write_to_json(filename, data):
    """
    Write data to a JSON file.

    Args:
        filename (str): The name of the JSON file to create or overwrite.
        data (object): The data to be written to the JSON file. It should be JSON-serializable.

    Raises:
        IOError: If an error occurs while writing to the file.

    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        # Handle file write errors
        raise IOError(f"An error occurred while writing to {filename}: {e}")