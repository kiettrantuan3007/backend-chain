import json
def import_dt(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

