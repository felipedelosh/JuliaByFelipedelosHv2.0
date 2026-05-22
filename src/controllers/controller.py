"""
FelipedelosH


main controller
"""
import sys
import os
from os import scandir

# INFRAESTRUCTURE
from src.infraestructure.configManager import ConfigManager


class Controller:
    def __init__(self) -> None:
        self.path = str(os.path.abspath(os.path.dirname(sys.argv[0])))
        self.config = ConfigManager()
        print("Gretting from Controller")
        print(f"MAIN Path: {self.path}")
        print(f"Config: {self.config._data}")
        pass

    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def getAllFilesNamesByExt(self, path, ext):
        """
        Return all files names of data folder with the specified extension
        """
        try:
            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ext in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return None
