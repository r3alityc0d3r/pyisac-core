import json

def load(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data
