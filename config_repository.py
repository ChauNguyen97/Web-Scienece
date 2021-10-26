import pandas as pd
import json


class ConfigRepository:
    def __init__(self):
        with open("config.json") as f:
            self._pattern = json.load(f)

    def getPatternByUrl(self, url):
        for key in self._pattern.keys():
            if url.find(key) != -1:
                return self._pattern[key]
        return {}
