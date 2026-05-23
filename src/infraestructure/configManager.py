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
        self._colors_arr = []
        self.load()

    def load(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {}

        if os.path.exists("data/colors.txt") and not self._data.get("black_and_white_mode"):
            with open("data/colors.txt", "r", encoding="utf-8") as f:
                for i in f.read().split('\n'):
                    if str(i).strip() != "":
                        self._colors_arr.append(str(i).strip())
        else:
            self._colors_arr = ["white", "black"]
