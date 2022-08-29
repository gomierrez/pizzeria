import json
from modules import FILE_PATH


def read_file():
    """
    Reads the file and returns the content as a list.
    """
    try:
        with open(FILE_PATH, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("El Archivo No Existe!")
        return {"ingredients":[]}


def write_file(content):
    with open(FILE_PATH, 'w', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(content, indent=4))
    return False, ""
