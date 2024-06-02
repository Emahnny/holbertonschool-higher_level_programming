
import json

def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary to JSON and saves it to a file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it to a dictionary.

    Args:
        filename (str): The name of the file to load the JSON data from.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
