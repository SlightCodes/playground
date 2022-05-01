import json
from Slide import replace
import logging


class Dictionary(dict):
    def __init__(self):

        self.d1 = ({"firstName": "default", "lastName": "default", "age": 0,
                    "gender": {"male": "unspecified", "female": "unspecified"},
                    "siblingAges": [0, 0]})

jsonDict = Dictionary()

jsonDict.d1["lastName"] = replace.update["lastName"]
jsonDict.d1["age"] = replace.update["age"]
jsonDict.d1["firstName"] = replace.update["firstName"]
jsonDict.d1["siblingAges"] = replace.update["siblingAges"]
jsonDict.d1["gender"]["female"] = replace.update["gender"]

def convertJson():
    with open("outfile.json", "w") as outfile:
        json.dump(jsonDict.d1, outfile, indent=4)

convertJson()


