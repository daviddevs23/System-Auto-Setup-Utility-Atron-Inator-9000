import json

# Reads in json and will return dict
def readJson(file):
    data = {}
    try:
        with open(file) as dataFile:
            data = json.load(dataFile)
    except Exception as e:
        print(f"There was an error in {file}")
        print(f"\t{e}")
        data = False

    return data
