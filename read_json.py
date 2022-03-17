import json
import os
import logging


def read_json(file):
    base = os.getcwd()
    full_path = os.path.join(base, file)
    logging.info(f'full_path:{full_path}')
    # Opening JSON file
    with open(full_path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return json_object
