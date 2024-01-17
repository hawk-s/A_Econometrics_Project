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
    

#use in case one wants to prevent overwriting the same file each time the code runs:
'''
import json
import os

def write_to_json(filename, data):
    """
    Write data to a JSON file if the file does not already exist.

    Args:
        filename (str): The name of the JSON file to create.
        data (object): The data to be written to the JSON file. It should be JSON-serializable.

    Returns:
        str: Message indicating the result of the operation.

    Raises:
        IOError: If an error occurs while writing to the file.
    """
    if os.path.exists(filename):
        # File already exists, skip writing
        return f"File '{filename}' already exists. Skipping file creation."

    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f"File '{filename}' successfully created."
    except IOError as e:
        # Handle file write errors
        raise IOError(f"An error occurred while writing to {filename}: {e}")
'''