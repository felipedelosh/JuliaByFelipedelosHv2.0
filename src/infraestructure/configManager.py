"""
FelipedelosH

read config.json
"""
import json
import os

class ConfigManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self._data = {}
        self._colors = ""
        self.load()

    def load(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {}

        if os.path.exists("data/colors.txt"):
            with open("data/colors.txt", "r", encoding="utf-8") as f:
                self._colors = f.read()
        else:
            self._colors = "white\nblack"
